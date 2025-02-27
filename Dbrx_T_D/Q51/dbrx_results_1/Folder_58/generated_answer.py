import re
from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        string = re.sub('\\W+', '', string)
        if len(string) >= 3:
            anagram = ''.join(sorted(string.lower()))
            if anagram not in anagrams:
                anagrams.append(anagram)
            else:
                anagrams.remove(anagram)
    return len(anagrams) <= 60