from collections import defaultdict

def if_contains_anagrams(strs):
    anagram_count = defaultdict(int)
    for s in strs:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagram_count[key] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) <= 131