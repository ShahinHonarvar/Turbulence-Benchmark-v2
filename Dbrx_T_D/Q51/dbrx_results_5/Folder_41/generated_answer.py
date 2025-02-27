import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_s = tuple(sorted(re.findall('[a-zA-Z]{3,}', s.lower())))
        anagrams[sorted_s].append(s)
    return sum((1 for a in anagrams.values() if len(a) > 52)) == 0