from collections import Counter

def if_contains_anagrams(strings):
    anagram_counter = Counter()
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            anagram_counter[tuple(sorted(s))] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counter.values()))
    return anagram_pairs >= 84