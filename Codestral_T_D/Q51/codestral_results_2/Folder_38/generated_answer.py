from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        counter[tuple(sorted(s))] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in counter.values()))
    return anagram_pairs <= 416