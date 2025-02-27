import itertools
from collections import Counter

def if_contains_anagrams(strings):
    anagrams_count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if Counter(sorted_string) in ["'a':2", "'e':2", "'i':2", "'o':2", "'u':2", "' ':2"]:
                anagrams_count += 1
                if anagrams_count > 6:
                    return False
    return True