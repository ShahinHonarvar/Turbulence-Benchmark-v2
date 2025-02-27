import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string in list_of_strings:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3 and sorted_string not in anagrams:
            anagrams.add(sorted_string)
    return len(anagrams) <= 21