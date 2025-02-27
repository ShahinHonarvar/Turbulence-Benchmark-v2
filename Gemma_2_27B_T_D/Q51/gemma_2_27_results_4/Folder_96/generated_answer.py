def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            a = sorted(strs[i].lower())
            b = sorted(strs[j].lower())
            if a == b and len(a) >= 3:
                count += 1
    return count <= 2