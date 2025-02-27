import string
from collections import Counter

def if_contains_anagrams(lst):
    lst = [s.lower().strip(string.punctuation) for s in lst if len(s) >= 3]
    count = sum((1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if Counter(lst[i]) == Counter(lst[j])))
    return count <= 54