import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    english_letters = set(string.ascii_lowercase)
    for string_in_list in list_of_strings:
        string_in_list = string_in_list.lower()
        if len(string_in_list) < 3:
            continue
        sorted_string = ''.join(sorted((c for c in string_in_list if c in english_letters)))
        anagrams.add(sorted_string)
    return len(anagrams) <= 58