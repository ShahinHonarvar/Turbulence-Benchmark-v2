import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = re.sub('\\W+', '', string).lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    count = 0
    for anagram in anagrams.values():
        count += anagram * (anagram - 1) // 2
        if count > 59:
            return False
    return True