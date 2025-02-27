import re
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for string in lst:
        string = re.sub('\\W+', '', string).lower()
        if len(string) < 3:
            continue
        anagram = ''.join(sorted(string))
        anagrams.append(anagram)
    anagrams_counter = Counter(anagrams)
    return sum(anagrams_counter.values()) <= 36