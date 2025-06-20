from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_count[sorted_s] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_count.values() if count > 1))
    return pair_count >= 38