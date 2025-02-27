from collections import Counter
from itertools import chain, combinations

def if_contains_anagrams(lst):
    counter_set = [Counter(sorted(word.lower())) for word in lst if len(word) >= 3]
    num_pairs = sum((k * (k - 1) // 2 for k in counter_set if k > 1))
    return num_pairs <= 401