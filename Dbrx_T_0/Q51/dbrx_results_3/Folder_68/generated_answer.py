import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string_ in list_of_strings:
        sorted_string = ''.join(sorted(string_.lower()))
        if len(sorted_string) >= 3 and all((char in string.ascii_letters for char in sorted_string)):
            anagrams.add(sorted_string)
    return len(anagrams) <= 94