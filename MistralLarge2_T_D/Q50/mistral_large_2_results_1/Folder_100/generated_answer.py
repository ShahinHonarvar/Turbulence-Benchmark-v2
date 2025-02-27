from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs >= 95