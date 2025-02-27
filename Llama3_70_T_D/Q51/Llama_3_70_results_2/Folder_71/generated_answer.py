from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = defaultdict(int)
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams_count[sorted_s] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return pairs_count <= 9