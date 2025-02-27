from collections import Counter

def if_contains_anagrams(lst):
    num_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()) and len(lst[i]) >= 3:
                num_pairs += 1
        if num_pairs > 41:
            return False
    return num_pairs