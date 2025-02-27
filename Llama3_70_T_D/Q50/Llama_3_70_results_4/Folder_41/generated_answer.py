def if_contains_anagrams(lst):
    count = 0
    lst = [x.lower() for x in lst if len(x) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                count += 1
    return count >= 75