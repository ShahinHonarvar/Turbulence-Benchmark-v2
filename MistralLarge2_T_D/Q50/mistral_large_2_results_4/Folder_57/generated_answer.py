from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        anagram_count[key] += 1
    total_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return total_pairs >= 50