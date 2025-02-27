def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if len(strs[i]) >= 3 and len(strs[j]) >= 3:
                s1 = sorted(strs[i].lower())
                s2 = sorted(strs[j].lower())
                if s1 == s2:
                    count += 1
    return count <= 57