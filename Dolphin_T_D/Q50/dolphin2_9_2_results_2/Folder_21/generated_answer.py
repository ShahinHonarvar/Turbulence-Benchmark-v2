from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagrams = 0
    for i in range(len(list_of_strings)):
        string1 = list_of_strings[i]
        for j in range(i + 1, len(list_of_strings)):
            string2 = list_of_strings[j]
            if len(string1) >= 3 and len(string2) >= 3 and (Counter(string1.lower()) == Counter(string2.lower())):
                anagrams += 1
        if anagrams >= 136:
            return True
    return False