import string

def if_contains_anagrams(string_list):
    anagrams = set()
    english_letters = set(string.ascii_lowercase)
    for string in string_list:
        if len(string) < 3:
            continue
        string = string.lower()
        sorted_string = ''.join(sorted((c for c in string if c in english_letters)))
        anagrams.add(sorted_string)
    return len(anagrams) <= 9