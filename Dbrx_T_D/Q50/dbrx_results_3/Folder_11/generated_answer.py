import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = 0
    anagrams_map = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(re.findall('\\\\w', string.lower())))
        anagrams_map[sorted_string].append(string)
    for anagrams in anagrams_map.values():
        if len(anagrams) > 1:
            anagrams_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagrams_count >= 28