import re
from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) < 3:
            continue
        string = re.sub('[^a-zA-Z]', '', string).lower()
        if len(Counter(string)) != len(string):
            anagram = ''.join(sorted(string))
            if anagram not in anagrams:
                anagrams.append(anagram)
    return len(anagrams) <= 93