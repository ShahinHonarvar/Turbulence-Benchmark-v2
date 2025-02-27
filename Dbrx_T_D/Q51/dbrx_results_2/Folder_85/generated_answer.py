import string

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    alphabet = set(string.ascii_letters.lower())
    for string in list_of_strings:
        string = ''.join(filter(alphabet.__contains__, string.lower()))
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        anagrams.add(sorted_string)
    return len(anagrams) <= 276