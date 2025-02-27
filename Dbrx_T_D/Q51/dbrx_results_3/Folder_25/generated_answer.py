import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    english_letters = set(string.ascii_lowercase)
    for string_in_list in list_of_strings:
        if len(string_in_list) < 3:
            continue
        string_in_list = string_in_list.lower()
        sorted_string = ''.join(sorted(filter(english_letters.__contains__, string_in_list)))
        if len(sorted_string) > 1:
            anagrams.add(sorted_string)
    return len(anagrams) <= 67