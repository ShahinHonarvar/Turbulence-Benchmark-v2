import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower(), key=lambda char: char in string.ascii_letters))
        if len(sorted_string) >= 3:
            anagrams.add(sorted_string)
    return len(anagrams) <= 35