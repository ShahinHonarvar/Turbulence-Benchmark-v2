def if_contains_anagrams(lst):
    count = 0
    lst = [s.lower() for s in lst]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i]) == sorted(lst[j])):
                count += 1
                if count == 26:
                    return True
    return False