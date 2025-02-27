import itertools
from collections import Counter

def if_contains_anagrams(lst):
    result = False
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            counter_lst = Counter(lst[i].lower())
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3 and Counter(lst[j].lower()) == counter_lst:
                    result = True
        if result:
            return result
    return result