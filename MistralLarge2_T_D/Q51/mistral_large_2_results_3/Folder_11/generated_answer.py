from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_count[sorted_s] += 1
    pairs_of_anagrams = sum((count > 1 for count in anagram_count.values()))
    return pairs_of_anagrams <= 41