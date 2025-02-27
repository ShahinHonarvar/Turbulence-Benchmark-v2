from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_count = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams_count[sorted_s] += 1
    pairs_count = sum((count - 1 for count in anagrams_count.values() if count > 1))
    return pairs_count <= 4