from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_chars = ''.join(sorted(s.lower()))
            anagram_counts[sorted_chars] += 1
    pair_count = 0
    for count in anagram_counts.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
            if pair_count >= 81:
                return True
    return False