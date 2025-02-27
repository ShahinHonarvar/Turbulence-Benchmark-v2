from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    anagram_count = 0
    word_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_dict[sorted_word].append(word)
    for group in word_dict.values():
        if len(group) > 1:
            anagram_count += len(list(combinations(group, 2)))
    return anagram_count <= 29