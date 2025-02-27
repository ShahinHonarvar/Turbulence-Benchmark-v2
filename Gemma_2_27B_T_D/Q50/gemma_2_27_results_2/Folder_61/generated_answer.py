from collections import Counter

def if_contains_anagrams(strs):
    anagram_pairs = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            str1 = strs[i].lower()
            str2 = strs[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if Counter(str1) == Counter(str2):
                    anagram_pairs += 1
    return anagram_pairs >= 8