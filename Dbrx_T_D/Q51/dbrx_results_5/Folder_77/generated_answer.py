import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    max_pairs = 17
    for string_elem in list_of_strings:
        if len(string_elem) < 3 or not string_elem.isalpha() or string_elem.lower() in anagrams:
            continue
        sorted_string = ''.join(sorted(string_elem.lower()))
        anagrams.add(sorted_string)
    if len(anagrams) > max_pairs:
        return False
    else:
        return True