import re
from collections import Counter

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string in strings_list:
        if len(string) < 3:
            continue
        string = re.findall('\\w', string.lower())
        if len(string) > 1:
            string = ''.join(sorted(string))
            anagrams_count += 1 if anagrams_count % 2 == 0 else -1
    return anagrams_count <= 64