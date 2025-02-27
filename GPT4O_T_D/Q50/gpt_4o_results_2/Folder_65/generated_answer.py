from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_groups[sorted_str] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_groups.values()))
    return anagram_pairs >= 94