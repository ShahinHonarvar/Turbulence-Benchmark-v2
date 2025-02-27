from itertools import combinations
from collections import Counter

def if_contains_anagrams(lst):
    sorted_str_list = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    pairs = list(combinations(sorted_str_list, 2))
    counter = sum((1 for pair in pairs if pair[0] == pair[1]))
    return counter <= 79