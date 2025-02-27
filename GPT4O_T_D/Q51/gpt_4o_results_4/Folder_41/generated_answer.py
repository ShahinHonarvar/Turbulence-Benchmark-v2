from collections import Counter, defaultdict

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_map = defaultdict(int)
    for s in lst:
        sorted_s = ''.join(sorted(filter(str.isalpha, s)))
        anagram_map[sorted_s] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_map.values() if count > 1))
    return pairs <= 52