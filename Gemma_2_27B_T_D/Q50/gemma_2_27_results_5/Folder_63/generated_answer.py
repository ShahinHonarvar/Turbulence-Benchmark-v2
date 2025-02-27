def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if len(strs[i]) >= 3 and len(strs[j]) >= 3 and (sorted(strs[i].lower()) == sorted(strs[j].lower())):
                count += 1
    return count >= 89