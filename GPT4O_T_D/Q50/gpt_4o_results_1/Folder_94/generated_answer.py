from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    strings_lower = [s.lower() for s in strings]
    for s in strings_lower:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_counts[sorted_s] += 1
    pairs_count = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
        if pairs_count >= 46:
            return True
    return False