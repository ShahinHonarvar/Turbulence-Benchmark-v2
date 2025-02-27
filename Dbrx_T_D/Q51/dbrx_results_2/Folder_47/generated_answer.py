import re

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = string.lower()
        string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string)))
        if string:
            anagrams[string] = anagrams.get(string, 0) + 1
    return sum(anagrams.values()) <= 366