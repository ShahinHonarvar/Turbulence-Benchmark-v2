from collections import Counter

def if_contains_anagrams(strings):
    counts = Counter()
    for string in strings:
        normalized = ''.join(sorted(string.lower())).strip()
        if len(normalized) >= 3:
            counts[normalized] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in counts.values()))
    return anagram_pairs <= 35