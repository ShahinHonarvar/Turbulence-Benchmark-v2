from collections import defaultdict

def if_contains_anagrams(strings):
    pairs_count = 0
    normalized = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            normalized[key] += 1
    for count in normalized.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
    return pairs_count >= 10