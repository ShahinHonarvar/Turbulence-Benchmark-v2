def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    cnt = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                cnt += 1
    return cnt >= 60