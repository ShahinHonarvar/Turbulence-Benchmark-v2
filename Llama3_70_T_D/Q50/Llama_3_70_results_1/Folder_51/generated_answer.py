from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_count[sorted_string] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) >= 39