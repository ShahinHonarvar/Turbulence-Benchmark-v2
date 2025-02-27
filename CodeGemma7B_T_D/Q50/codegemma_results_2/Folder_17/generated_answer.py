from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    count = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 2:
            count += len(list(combinations(anagram_group, 2)))
    return count >= 97