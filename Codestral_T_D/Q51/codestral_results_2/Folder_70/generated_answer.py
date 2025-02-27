from collections import Counter

def if_contains_anagrams(string_list):
    anagram_counter = Counter([''.join(sorted(s.lower())) for s in string_list if len(s) >= 3])
    return sum((v * (v - 1) // 2 for v in anagram_counter.values())) <= 97