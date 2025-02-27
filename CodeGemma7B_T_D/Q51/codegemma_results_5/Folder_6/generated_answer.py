def if_contains_anagrams(str_lst):
    str_lst = [s.lower() for s in str_lst]
    str_lst = [s for s in str_lst if len(s) >= 3]
    str_lst.sort(key=len)
    pairs = []
    for i in range(len(str_lst) - 1):
        for j in range(i + 1, len(str_lst)):
            if sorted(str_lst[i]) == sorted(str_lst[j]):
                pairs.append((str_lst[i], str_lst[j]))
    return len(pairs) <= 86