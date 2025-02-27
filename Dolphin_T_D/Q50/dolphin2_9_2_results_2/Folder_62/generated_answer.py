def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            lst1 = ''.join(lst[i].lower().split())
            lst2 = ''.join(lst[j].lower().split())
            if len(lst1) >= 3 and len(lst2) >= 3 and (sorted(lst1) == sorted(lst2)):
                pairs += 1
    return pairs >= 43