from collections import defaultdict
from itertools import combinations
from math import factorial

def if_contains_anagrams(lst):
    anagram_count = 0
    str_len_dict = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            str_len_dict[len(s)].append(sorted_str)
    for i in str_len_dict.values():
        i.sort()
        for j in range(len(i) - 1):
            if i[j] == i[j + 1]:
                anagram_count += 1
    return anagram_count >= 55