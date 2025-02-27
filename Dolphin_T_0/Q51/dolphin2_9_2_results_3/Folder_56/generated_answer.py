def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = sorted(lst[i].lower())
            s2 = sorted(lst[j].lower())
            s1 = ''.join(s1)
            s2 = ''.join(s2)
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (s1 == s2):
                count += 1
                if count > 11:
                    return False
    return True