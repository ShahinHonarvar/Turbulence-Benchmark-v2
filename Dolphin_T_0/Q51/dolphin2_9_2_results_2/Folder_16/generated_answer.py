import re
from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            sorted_str1 = sorted(re.sub('[^a-z]', '', lst[i].lower()))
            sorted_str2 = sorted(re.sub('[^a-z]', '', lst[j].lower()))
            if Counter(sorted_str1) == Counter(sorted_str2):
                anagram_pairs += 1
    return anagram_pairs <= 24