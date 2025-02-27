from collections import defaultdict

def if_contains_anagrams(strings):
    normalized = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            normalized[sorted_s].append(s_lower)
    anagram_pairs = 0
    for group in normalized.values():
        count = len(group)
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 289:
                return False
    return anagram_pairs <= 289