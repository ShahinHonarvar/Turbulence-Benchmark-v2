import string

def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        string = ''.join(filter(str.isalpha, string.lower()))
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        anagrams.add(sorted_string)
    return len(anagrams) <= 74