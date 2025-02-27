from collections import Counter

def if_contains_anagrams(strings):
    anagram_counter = Counter()
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagram_counter[key] += 1
    pair_count = sum((n * (n - 1) // 2 for n in anagram_counter.values()))
    return pair_count <= 36