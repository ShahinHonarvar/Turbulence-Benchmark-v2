from collections import Counter

def if_contains_anagrams(strs):
    anagrams = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            str1 = strs[i].lower()
            str2 = strs[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if Counter(str1) == Counter(str2):
                    anagrams += 1
    return anagrams <= 26