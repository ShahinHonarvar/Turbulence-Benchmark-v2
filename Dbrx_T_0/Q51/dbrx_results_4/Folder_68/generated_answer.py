import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string_to_check in list_of_strings:
        if len(string_to_check) < 3:
            continue
        sorted_string = ''.join(sorted(string_to_check.lower()))
        if sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) > 94