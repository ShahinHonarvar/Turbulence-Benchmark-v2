import re

def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        string = re.sub('[^\\\\w]', '', string).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = [string]
        else:
            anagrams[sorted_string].append(string)
    anagram_pairs = sum([len(value) - 1 for value in anagrams.values()])
    return anagram_pairs >= 96