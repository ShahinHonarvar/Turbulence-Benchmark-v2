def if_contains_anagrams(lst):
    lst = [i.lower() for i in lst if len(i) >= 3]
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                count += 1
                if count >= 30:
                    return True
    return False