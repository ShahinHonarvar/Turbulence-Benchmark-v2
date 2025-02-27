import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string_ in list_of_strings:
        sorted_string = ''.join(sorted(string_.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(sorted_string) >= 3:
            anagrams.add(sorted_string)
    return len(anagrams) <= 116