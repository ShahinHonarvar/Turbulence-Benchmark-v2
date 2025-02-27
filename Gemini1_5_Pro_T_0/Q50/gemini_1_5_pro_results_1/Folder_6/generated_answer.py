from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            string1 = list_of_strings[i].lower()
            string2 = list_of_strings[j].lower()
            if len(string1) >= 3 and len(string2) >= 3 and (Counter(string1) == Counter(string2)):
                anagram_count += 1
    if anagram_count >= 26:
        return True
    else:
        return False