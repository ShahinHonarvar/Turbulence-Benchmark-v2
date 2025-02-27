def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if len(strs[i]) >= 3 and len(strs[j]) >= 3:
                str1 = strs[i].lower()
                str2 = strs[j].lower()
                if sorted(str1) == sorted(str2):
                    count += 1
    return count <= 407