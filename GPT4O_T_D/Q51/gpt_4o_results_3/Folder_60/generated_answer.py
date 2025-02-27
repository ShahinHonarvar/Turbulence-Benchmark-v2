from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagrams[sorted_str(s)].append(s)
    pair_count = 0
    for group in anagrams.values():
        n = len(group)
        if n > 1:
            pair_count += n * (n - 1) // 2
            if pair_count > 77:
                return False
    return pair_count <= 77