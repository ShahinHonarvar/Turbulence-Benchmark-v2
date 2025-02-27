def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    counter = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                counter += 1
    return counter >= 20