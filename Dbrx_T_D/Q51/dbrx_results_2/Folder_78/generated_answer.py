import string

def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3 and sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) > 36