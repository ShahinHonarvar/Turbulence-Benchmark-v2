from collections import defaultdict
from itertools import combinations
from string import ascii_lowercase

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        key = ''.join(sorted([c.lower() for c in word if c.isalpha()]))
        anagrams[key].append(word)
    count = 0
    for key, group in anagrams.items():
        if len(group) >= 3:
            count += len(combinations(group, 2))
    return count <= 21