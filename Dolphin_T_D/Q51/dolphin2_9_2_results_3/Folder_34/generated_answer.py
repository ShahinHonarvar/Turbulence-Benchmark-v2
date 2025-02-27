from collections import Counter

def if_contains_anagrams(list_of_strings):
    count_anagrams = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i].lower()[::-1]
            str2 = list_of_strings[j].lower()[::-1]
            if len(str1) >= 3 and len(str2) >= 3 and (Counter(str1) == Counter(str2)):
                count_anagrams += 1
    return count_anagrams <= 401