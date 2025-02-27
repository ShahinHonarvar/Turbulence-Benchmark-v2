from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = sorted_lower(s)
            anagrams[key] += 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
        if count > 41:
            return False
    return True