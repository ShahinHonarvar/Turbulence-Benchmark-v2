import re

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        string = re.sub('\\W+', '', string).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagrams:
            anagrams.append(sorted_string)
    return len(anagrams) <= 10