import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    english_letters = set(string.ascii_lowercase)
    for string_ in list_of_strings:
        string_ = string_.lower()
        chars = {char for char in string_ if char in english_letters}
        if len(chars) >= 3:
            anagram = ''.join(sorted(chars))
            if anagram in anagrams:
                if len(anagrams) >= 28:
                    return True
            else:
                anagrams.add(anagram)
    return False