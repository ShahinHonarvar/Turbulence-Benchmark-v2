from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for string in strings:
        normalized = ''.join(sorted(string.lower()))
        if len(normalized) >= 3:
            anagrams[normalized] += 1
    count = 0
    for key in anagrams:
        pairs = anagrams[key] * (anagrams[key] - 1) // 2
        count += pairs
        if count >= 25:
            return True
    return False