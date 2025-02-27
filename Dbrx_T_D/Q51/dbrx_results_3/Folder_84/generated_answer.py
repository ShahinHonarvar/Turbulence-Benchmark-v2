import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string_in_list in list_of_strings:
        if len(string_in_list) < 3:
            continue
        string_in_list = string_in_list.lower()
        sorted_string = ''.join(sorted(string_in_list))
        anagrams.add(sorted_string)
    return len(anagrams) <= 16