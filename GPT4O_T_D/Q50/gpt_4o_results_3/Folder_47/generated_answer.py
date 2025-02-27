from collections import defaultdict

def if_contains_anagrams(strings):
    counter = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        counter[sorted_str] += 1
    anagram_pairs = 0
    for count in counter.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 47