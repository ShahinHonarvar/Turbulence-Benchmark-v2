import re

def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        string = re.sub('\\W+', '', string).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) > 22