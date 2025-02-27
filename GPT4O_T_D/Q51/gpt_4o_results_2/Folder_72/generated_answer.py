from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_key(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_groups[sorted_key(s)].append(s)
    anagram_pairs_count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            anagram_pairs_count += n * (n - 1) // 2
    return anagram_pairs_count <= 188