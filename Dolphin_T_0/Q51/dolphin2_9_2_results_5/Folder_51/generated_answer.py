def if_contains_anagrams(lst):
    count = 0
    for i, s1 in enumerate(lst):
        for s2 in lst[i + 1:]:
            s1 = s1.lower()
            s2 = s2.lower()
            if len(s1) >= 3 and sorted(s1) == sorted(s2):
                count += 1
                if count > 58:
                    return False
    return True