import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string_ in list_of_strings:
        if len(string_) < 3:
            continue
        string_ = string_.lower()
        sorted_string = ''.join(sorted(string_))
        if sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) <= 74