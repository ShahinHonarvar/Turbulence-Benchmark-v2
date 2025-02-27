import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for string in string_list:
        string = string.lower()
        if len(string) < 3 or not string.isalpha():
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) <= 173