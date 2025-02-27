import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string_to_check in list_of_strings:
        if len(string_to_check) < 3:
            continue
        string_to_check = string_to_check.lower()
        sorted_string = ''.join(sorted(string_to_check))
        if sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) > 474