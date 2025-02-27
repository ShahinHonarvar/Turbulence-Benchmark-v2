import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for string in string_list:
        normalized_string = ''.join(sorted(string.lower())).encode('utf-8')
        if len(normalized_string) >= 3 and normalized_string in anagrams:
            return False
        anagrams.add(normalized_string)
    return len(anagrams) <= 52