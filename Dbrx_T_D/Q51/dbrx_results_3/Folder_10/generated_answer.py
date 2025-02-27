from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagrams = []
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams.append(sorted_string)
    return len(anagrams) <= 21