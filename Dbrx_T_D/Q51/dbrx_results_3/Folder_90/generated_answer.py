import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string_ in list_of_strings:
        string_ = ''.join(sorted(string_.lower())).encode('utf-8')
        string_ = string_.translate(str.maketrans('', '', string.punctuation + string.digits))
        if len(string_) >= 3:
            anagrams.add(string_)
    return len(anagrams) <= 147