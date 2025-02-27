from collections import Counter

def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs) - 1):
        for j in range(i + 1, len(strs)):
            s1 = strs[i].lower()
            s2 = strs[j].lower()
            if len(s1) >= 3 and len(s2) >= 3 and (Counter(s1) == Counter(s2)):
                count += 1
    return count <= 276