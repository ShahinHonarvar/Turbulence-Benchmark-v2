import string

def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        sorted_string = ''.join(sorted(string.lower())).encode('utf-8')
        if len(sorted_string) >= 3:
            anagrams.add(sorted_string)
    return len(anagrams) <= 116