import re

def if_contains_anagrams(lst):
    anagrams = []
    for s in lst:
        sorted_s = ''.join(sorted(filter(str.islower, s))).lower()
        if len(sorted_s) >= 3:
            anagrams.append(sorted_s)
    anagram_pairs = 0
    for i in range(len(anagrams) - 1):
        for j in range(i + 1, len(anagrams)):
            if anagrams[i] == anagrams[j]:
                anagram_pairs += 1
                if anagram_pairs > 49:
                    return False
    return True