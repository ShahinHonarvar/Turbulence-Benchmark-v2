from collections import Counter
import itertools

def if_contains_anagrams(lst):
    count = 0
    for i, word1 in enumerate(lst):
        if len(word1) >= 3:
            for word2 in lst[i + 1:]:
                if len(word2) >= 3:
                    if sorted(word1.lower()) == sorted(word2.lower()):
                        count += 1
    return count <= 40