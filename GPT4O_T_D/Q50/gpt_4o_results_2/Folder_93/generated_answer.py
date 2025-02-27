from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        normalized = ''.join(sorted(s.lower()))
        if len(normalized) >= 3:
            anagram_count[normalized] += 1
    pairs_count = 0
    for count in anagram_count.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
        if pairs_count >= 18:
            return True
    return False