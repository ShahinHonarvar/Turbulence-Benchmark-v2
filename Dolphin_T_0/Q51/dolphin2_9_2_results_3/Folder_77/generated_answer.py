def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst[i] = lst[i].lower()
                lst[j] = lst[j].lower()
                if sorted(lst[i]) == sorted(lst[j]):
                    pairs += 1
    return pairs <= 17