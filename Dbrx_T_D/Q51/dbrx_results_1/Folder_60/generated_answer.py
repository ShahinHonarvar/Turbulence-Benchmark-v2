import re
from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagrams = []
    for string in list_of_strings:
        string = re.sub('\\W+', '', string).lower()
        if len(string) >= 3:
            anagram = tuple(sorted(string))
            if anagram not in anagrams:
                anagrams.append(anagram)
    return len(anagrams) <= 77