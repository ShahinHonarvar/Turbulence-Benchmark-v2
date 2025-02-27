from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1, str2 = (list_of_strings[i], list_of_strings[j])
            if len(str1) >= 3 and len(str2) >= 3 and (str1.lower() != str2.lower()):
                str1, str2 = (Counter(str1.lower()), Counter(str2.lower()))
                if str1 == str2:
                    anagram_pairs += 1
    return anagram_pairs <= 206