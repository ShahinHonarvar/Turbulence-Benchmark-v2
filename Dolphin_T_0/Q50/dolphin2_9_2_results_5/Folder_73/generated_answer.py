def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    count = 0
    for x in range(len(lst)):
        for y in range(x + 1, len(lst)):
            if sorted(lst[x]) == sorted(lst[y]):
                count += 1
    return count >= 91