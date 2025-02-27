from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_groups = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_groups[sorted_s] += 1
    pair_count = 0
    for count in anagram_groups.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
        if pair_count >= 9:
            return True
    return False