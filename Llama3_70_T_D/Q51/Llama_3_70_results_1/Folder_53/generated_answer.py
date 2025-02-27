from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        anagram_key = ''.join(sorted(s_lower))
        anagram_count[anagram_key] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs_count <= 8