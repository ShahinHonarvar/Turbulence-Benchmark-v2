from collections import Counter

def if_contains_anagrams(list_of_strings):
    list_of_strings = [string.lower() for string in list_of_strings if len(string) >= 3]
    anagram_count = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if Counter(list_of_strings[i]) == Counter(list_of_strings[j]):
                anagram_count += 1
                if anagram_count > 81:
                    return False
    return True