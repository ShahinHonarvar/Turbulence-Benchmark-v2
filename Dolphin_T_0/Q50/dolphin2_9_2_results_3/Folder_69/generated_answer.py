from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    count += 1
                    if count >= 188:
                        return True
    return False