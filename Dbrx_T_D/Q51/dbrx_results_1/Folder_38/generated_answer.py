import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(re.findall('\\b\\w+\\b', s.lower())))
        anagrams[sorted_s].append(s)
    return len(anagrams) <= 416