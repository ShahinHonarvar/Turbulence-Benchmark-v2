import re
from collections import Counter

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1, string2 in combinations(strings_list, 2):
        if len(string1) >= 3 and len(string2) >= 3 and (Counter(re.findall('\\b\\w{3,}\\b', string1.lower())) == Counter(re.findall('\\b\\w{3,}\\b', string2.lower()))):
            anagrams_count += 1
        if anagrams_count > 68:
            return False
    return True