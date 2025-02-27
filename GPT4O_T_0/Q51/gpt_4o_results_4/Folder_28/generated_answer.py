from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            anagram_groups[sorted_s].append(s)
    anagram_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs > 78:
                return False
    return True