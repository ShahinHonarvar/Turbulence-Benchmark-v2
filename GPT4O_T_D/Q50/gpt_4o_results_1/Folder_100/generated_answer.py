from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sort_string(s)
            anagram_groups[sorted_s].append(s)
    anagram_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        if n >= 2:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 95