def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst) - 1):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3 and sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    pairs += 1
    return pairs >= 39