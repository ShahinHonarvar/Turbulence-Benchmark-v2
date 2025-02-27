import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for string_ in string_list:
        string_ = ''.join((c.lower() for c in string_ if c not in string.punctuation)).split()
        string_ = ''.join(sorted(string_))
        if len(string_) >= 3:
            anagrams.add(string_)
    return len(anagrams) <= 93