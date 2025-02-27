from collections import Counter

def if_contains_anagrams(lst):
    c = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    c += 1
                    break
    if c >= 65:
        return True
    else:
        return False