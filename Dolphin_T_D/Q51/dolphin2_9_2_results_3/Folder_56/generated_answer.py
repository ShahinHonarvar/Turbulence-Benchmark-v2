def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        s1 = lst[i].lower()
        for j in range(i + 1, len(lst)):
            s2 = lst[j].lower()
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
                count += 1
                if count > 11:
                    return False
    return count <= 11