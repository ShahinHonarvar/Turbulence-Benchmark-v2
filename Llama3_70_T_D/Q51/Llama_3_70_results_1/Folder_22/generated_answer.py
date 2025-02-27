from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagram_count[sorted_s] += 1
    count_pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return count_pairs <= 14