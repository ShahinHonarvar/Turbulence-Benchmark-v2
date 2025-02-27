from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    max_pairs = 35
    for string in strings:
        sorted_letters = ''.join(sorted(string.lower()))
        anagrams[sorted_letters].append(string)
    if len(anagrams) > max_pairs * 2:
        return False
    for pairs in anagrams.values():
        if len(pairs) >= 3:
            return True
    return False