import re

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = tuple(sorted(re.findall('\\\\b\\\\w+\\\\b', string.lower())))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = 0
            anagrams[sorted_string] += 1
    total_anagrams = sum([count // 2 for count in anagrams.values()])
    return total_anagrams >= 188