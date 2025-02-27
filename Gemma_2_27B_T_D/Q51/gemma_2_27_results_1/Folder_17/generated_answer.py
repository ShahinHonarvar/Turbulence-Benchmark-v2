def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            a = strs[i].lower()
            b = strs[j].lower()
            if len(a) >= 3 and len(b) >= 3 and (sorted(a) == sorted(b)):
                count += 1
    return count <= 22