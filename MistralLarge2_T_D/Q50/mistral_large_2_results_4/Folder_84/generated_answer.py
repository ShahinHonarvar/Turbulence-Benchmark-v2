from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    sorted_words = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            sorted_words[sorted_word].append(word)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in sorted_words.values() if len(group) > 1))
    return anagram_pairs >= 108