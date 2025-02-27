from itertools import combinations
from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    count = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    for words in anagram_dict.values():
        if len(words) > 1:
            count += len(list(combinations(words, 2)))
    return count >= 314