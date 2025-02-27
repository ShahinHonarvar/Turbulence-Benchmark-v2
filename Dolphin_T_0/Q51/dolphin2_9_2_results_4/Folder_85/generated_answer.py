from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i].lower()) >= 3 and len(lst[j].lower()) >= 3:
                if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    count += 1
    if count > 276:
        return False
    else:
        return True