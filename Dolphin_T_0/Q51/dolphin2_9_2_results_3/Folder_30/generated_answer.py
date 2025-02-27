from collections import Counter

def if_contains_anagrams(lst):
    pair_count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3:
                    lst1 = Counter(lst[i].lower())
                    lst2 = Counter(lst[j].lower())
                    if lst1 == lst2:
                        pair_count += 1
                        if pair_count >= 28:
                            return True
    return False