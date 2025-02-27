from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = defaultdict(int)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams_count[sorted_s] += 1
    anagrams_count = sum((v * (v - 1) // 2 for v in anagrams_count.values()))
    return anagrams_count <= 59