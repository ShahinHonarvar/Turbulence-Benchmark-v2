import collections
import string

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = lst[i].lower()
            str2 = lst[j].lower()
            if len(str1) < 3 or len(str2) < 3:
                continue
            if collections.Counter(str1) == collections.Counter(str2):
                count += 1
    return count <= 173