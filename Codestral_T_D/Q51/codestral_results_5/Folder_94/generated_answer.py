from collections import Counter

def if_contains_anagrams(str_list):
    anagram_counter = Counter((''.join(sorted(s.lower())) for s in str_list if len(s) >= 3))
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_counter.values()))
    return anagram_pairs <= 181