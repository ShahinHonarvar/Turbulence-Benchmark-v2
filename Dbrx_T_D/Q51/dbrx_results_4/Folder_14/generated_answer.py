import string

def if_contains_anagrams(string_list):
    anagrams = set()
    english_letters = set(string.ascii_lowercase)
    for string in string_list:
        string = string.lower()
        chars = set(string)
        if len(chars) < 3:
            continue
        chars -= english_letters
        if ' ' in chars:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) > 474