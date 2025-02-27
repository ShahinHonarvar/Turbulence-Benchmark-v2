from collections import defaultdict, deque
from itertools import combinations

def if_contains_anagrams(str_list):
    cnt = defaultdict(deque)
    for word in str_list:
        key = ''.join(sorted([x for x in word if x.isalpha() and len(x) >= 3], key=str.lower))
        cnt[key].append(word)
    return sum((len(v) >= 2 for v in cnt.values())) <= 16