import string

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        sorted_string = ''.join(sorted(filter(str.islower, string.lower())))
        if len(sorted_string) >= 3 and sorted_string not in anagrams:
            anagrams.append(sorted_string)
    return len(anagrams) <= 206