from collections import Counter

def if_contains_anagrams(lst_of_strings):
    anagram_pairs = 0
    for i in range(len(lst_of_strings)):
        str1 = lst_of_strings[i]
        for j in range(i + 1, len(lst_of_strings)):
            str2 = lst_of_strings[j]
            if len(str1) >= 3 and len(str2) >= 3 and (Counter(str1.lower()) == Counter(str2.lower())):
                anagram_pairs += 1
                if anagram_pairs > 58:
                    return False
    return True