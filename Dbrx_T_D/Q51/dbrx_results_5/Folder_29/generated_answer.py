import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    english_letters = set(string.ascii_lowercase)
    for string_in_list in list_of_strings:
        string_in_list = string_in_list.lower()
        sorted_string = ''.join(sorted((char for char in string_in_list if char in english_letters)))
        if len(sorted_string) >= 3:
            anagrams.add(sorted_string)
    if len(anagrams) > 318:
        return False
    else:
        return True