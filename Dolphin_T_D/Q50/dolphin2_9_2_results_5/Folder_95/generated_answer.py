def if_contains_anagrams(list_of_strings):
    anagrams = 0
    for string1 in list_of_strings:
        for string2 in list_of_strings:
            if len(string1) >= 3 and len(string2) >= 3 and (string1.lower() != string2.lower()) and (sorted(string1.lower()) == sorted(string2.lower())):
                anagrams += 1
                break
    return anagrams >= 93