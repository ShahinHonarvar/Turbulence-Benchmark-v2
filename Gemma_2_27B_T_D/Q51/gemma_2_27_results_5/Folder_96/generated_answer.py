def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            s1 = strs[i].lower()
            s2 = strs[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    count += 1
    if count <= 2:
        return True
    else:
        return False