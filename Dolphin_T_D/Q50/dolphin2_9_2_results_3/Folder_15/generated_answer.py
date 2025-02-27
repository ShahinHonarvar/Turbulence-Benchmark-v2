def if_contains_anagrams(lst):
    ana = 0
    pairs = len(lst) ** 2
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    ana += 1
    return ana >= 4