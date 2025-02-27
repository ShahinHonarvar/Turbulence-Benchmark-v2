from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    count = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3 and sorted(word1.lower()) == sorted(word2.lower()):
                    count += 1
    if count // 2 >= 21:
        return True
    else:
        return False