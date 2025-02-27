from collections import defaultdict

def if_contains_anagrams(strings):
    char_counts = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        char_counts[key] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in char_counts.values() if count > 1))
    return anagram_pairs <= 407