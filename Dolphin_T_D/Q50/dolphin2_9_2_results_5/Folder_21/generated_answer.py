def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    result = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                result += 1
    return result >= 136