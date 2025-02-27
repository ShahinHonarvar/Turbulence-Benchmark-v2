from collections import defaultdict

def if_contains_anagrams(lst):
    seen = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            seen[key] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in seen.values()))
    return anagram_pairs >= 40