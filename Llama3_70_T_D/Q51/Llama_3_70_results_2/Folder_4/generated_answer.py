from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_counter = defaultdict(int)
    for string in lst:
        s = ''.join(filter(str.isalpha, string)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagrams_counter[sorted_str] += 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams_counter.values()))
    return pairs <= 84