from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagram_count[key] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 113