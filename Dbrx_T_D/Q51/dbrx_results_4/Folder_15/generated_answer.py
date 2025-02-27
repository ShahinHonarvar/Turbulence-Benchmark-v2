import re
from collections import Counter

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1, string2 in combinations(strings_list, 2):
        if len(string1) >= 3 and len(string2) >= 3 and (Counter(re.findall('[a-zA-Z]{3,}', string1.lower())) == Counter(re.findall('[a-zA-Z]{3,}', string2.lower()))):
            anagrams_count += 1
        if anagrams_count > 20:
            return False
    return True