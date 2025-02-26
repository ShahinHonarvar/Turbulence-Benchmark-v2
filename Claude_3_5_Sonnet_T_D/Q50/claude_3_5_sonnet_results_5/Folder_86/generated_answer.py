from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for word in string_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs >= 115