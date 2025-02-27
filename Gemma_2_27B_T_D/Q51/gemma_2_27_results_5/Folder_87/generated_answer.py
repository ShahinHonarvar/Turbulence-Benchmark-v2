def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            w1 = strs[i].lower()
            w2 = strs[j].lower()
            if len(w1) >= 3 and len(w2) >= 3:
                if sorted(w1) == sorted(w2):
                    count += 1
    return count <= 392