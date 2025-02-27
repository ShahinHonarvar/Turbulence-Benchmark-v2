def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = ''.join(filter(str.isalpha, lst[i].lower()))
            s2 = ''.join(filter(str.isalpha, lst[j].lower()))
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
                count += 1
    return count <= 401