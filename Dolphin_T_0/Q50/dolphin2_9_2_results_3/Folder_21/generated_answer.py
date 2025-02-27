def if_contains_anagrams(lst):
    res = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                res += 1
    return res >= 136