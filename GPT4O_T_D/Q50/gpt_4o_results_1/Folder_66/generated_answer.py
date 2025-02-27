from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_counts[sorted_str] += 1
    anagram_pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 92:
                return True
    return anagram_pairs >= 92