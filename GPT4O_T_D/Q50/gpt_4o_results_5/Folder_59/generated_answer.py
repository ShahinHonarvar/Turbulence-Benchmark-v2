from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str] += 1
    pairs = 0
    for count in anagrams.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs >= 10:
                return True
    return False