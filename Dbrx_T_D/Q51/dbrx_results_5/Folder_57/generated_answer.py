import string

def if_contains_anagrams(list_of_strings):
    english_letters = set(string.ascii_letters.lower())
    anagrams = set()
    for string in list_of_strings:
        if len(string) < 3:
            continue
        string = ''.join(filter(english_letters.__contains__, string.lower()))
        sorted_string = ''.join(sorted(string))
        anagrams.add(sorted_string)
    if len(anagrams) > 74:
        return False
    else:
        return True