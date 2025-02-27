from collections import defaultdict

def if_contains_anagrams(strings):
    counter = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            counter[sorted_str] += 1
    anagram_count = sum((n * (n - 1) // 2 for n in counter.values() if n > 1))
    return anagram_count <= 38