import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for string in string_list:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3 and all((c in string for c in string if c not in string.punctuation)) and (sorted_string not in anagrams):
            anagrams.add(sorted_string)
            if len(anagrams) > 85:
                return False
    return True