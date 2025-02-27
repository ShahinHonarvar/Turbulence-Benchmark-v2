from collections import Counter

def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if len(strs[i]) >= 3 and len(strs[j]) >= 3:
                if sorted(Counter(strs[i].lower()).items()) == sorted(Counter(strs[j].lower()).items()):
                    count += 1
    return count <= 81