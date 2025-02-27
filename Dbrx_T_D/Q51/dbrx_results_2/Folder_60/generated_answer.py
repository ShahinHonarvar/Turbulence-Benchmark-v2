import string

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and all((char in string.ascii_letters for char in sorted_string)):
            anagrams.append(sorted_string)
    return len(set(anagrams)) <= 77