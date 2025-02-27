def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = sorted(lst[i].lower())
            s2 = sorted(lst[j].lower())
            if s1 == s2 and len(s1) >= 3:
                count += 1
                if count >= 44:
                    return True
    return False