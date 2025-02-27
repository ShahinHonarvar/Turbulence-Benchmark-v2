import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for string_ in string_list:
        if len(string_) < 3:
            continue
        string_ = string_.lower()
        sorted_string = ''.join(sorted(string_))
        if sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) > 97