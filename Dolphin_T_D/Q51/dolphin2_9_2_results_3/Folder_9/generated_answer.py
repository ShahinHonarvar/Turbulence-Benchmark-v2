from itertools import combinations
from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    for str1, str2 in combinations(lst, 2):
        if len(str1) >= 3 and len(str2) >= 3 and (Counter(str1.lower()) == Counter(str2.lower())):
            cnt += 1
    return cnt <= 475