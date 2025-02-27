from collections import Counter

def if_contains_anagrams(string_list):
    anagram_counter = Counter()
    for s in string_list:
        if len(s) >= 3:
            anagram_counter[tuple(sorted(s.lower()))] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_counter.values()))
    return anagram_pairs <= 74