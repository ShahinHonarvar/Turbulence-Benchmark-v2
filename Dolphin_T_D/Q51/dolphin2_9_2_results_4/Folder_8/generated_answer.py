import collections
import itertools
import math

def if_contains_anagrams(lst):
    count = 0
    lst = [x.replace(' ', '').lower() for x in lst]
    str_len = len(lst)
    for i in range(str_len):
        if len(lst[i]) >= 3:
            for j in range(i + 1, str_len):
                if len(lst[j]) >= 3:
                    if collections.Counter(lst[i]) == collections.Counter(lst[j]):
                        count += 1
    if count > 68:
        return True
    else:
        return False