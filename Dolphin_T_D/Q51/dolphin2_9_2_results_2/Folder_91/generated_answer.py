from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst_i = Counter(lst[i].lower())
                lst_j = Counter(lst[j].lower())
                if lst_i == lst_j:
                    count += 1
    return count <= 88