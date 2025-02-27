import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            string = re.sub('\\W+', '', string).lower()
            sorted_string = ''.join(sorted(string))
            if sorted_string not in anagrams:
                anagrams.append(sorted_string)
    return len(anagrams) <= 16