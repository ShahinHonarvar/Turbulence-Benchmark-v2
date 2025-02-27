from collections import Counter

def if_contains_anagrams(str_list):
    anagram_count = Counter()
    for s in str_list:
        s = s.lower()
        if len(s) < 3:
            continue
        anagram_count[tuple(sorted(s))] += 1
    return sum((v * (v - 1) // 2 for v in anagram_count.values())) >= 50