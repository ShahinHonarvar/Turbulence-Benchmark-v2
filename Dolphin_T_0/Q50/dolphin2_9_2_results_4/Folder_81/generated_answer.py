def if_contains_anagrams(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2 and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                res.append(1)
    return len(res) >= 16