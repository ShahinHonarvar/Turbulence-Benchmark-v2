from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if len(lst[j]) < 3:
                continue
            if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                count += 1
    return count >= 36