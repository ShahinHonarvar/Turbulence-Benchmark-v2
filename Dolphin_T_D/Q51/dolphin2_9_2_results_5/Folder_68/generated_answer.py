from collections import Counter

def if_contains_anagrams(list_str):
    anagram_pairs = 0
    for i in range(len(list_str)):
        for j in range(i + 1, len(list_str)):
            str1 = sorted(Counter(list_str[i].lower()))
            str2 = sorted(Counter(list_str[j].lower()))
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                anagram_pairs += 1
                if anagram_pairs >= 94:
                    return True
    if anagram_pairs <= 94:
        return False