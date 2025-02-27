import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string_ in list_of_strings:
        string_ = string_.lower()
        sorted_string = ''.join(sorted(string_))
        if len(sorted_string) >= 3 and sorted_string not in anagrams:
            anagrams.add(sorted_string)
    return len(anagrams) <= 88