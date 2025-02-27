from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(int)
    count = 0
    for s in strings:
        if len(s) >= 3:
            key = sorted_lower(s)
            count += anagram_map[key]
            anagram_map[key] += 1
    return count >= 28