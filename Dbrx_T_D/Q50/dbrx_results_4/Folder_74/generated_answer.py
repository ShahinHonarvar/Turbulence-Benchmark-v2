import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        normalized_string = re.sub('\\\\W+', '', string.lower())
        if len(normalized_string) >= 3:
            sorted_string = ''.join(sorted(normalized_string))
            anagrams[sorted_string].append(normalized_string)
    return len([value for value in anagrams.values() if len(value) >= 17]) > 0