from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if min(len(lst[i]), len(lst[j])) >= 3 and Counter(lst[i].lower()) == Counter(lst[j].lower()):
                pairs += 1
                if pairs >= 40:
                    return True
    return False