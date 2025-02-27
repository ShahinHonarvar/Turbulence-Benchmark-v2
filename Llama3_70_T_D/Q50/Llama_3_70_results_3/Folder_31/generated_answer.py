from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    anagram_count = 0
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        count[sorted_str] += 1
    for value in count.values():
        if value > 1:
            anagram_count += value * (value - 1) // 2
    return anagram_count >= 68