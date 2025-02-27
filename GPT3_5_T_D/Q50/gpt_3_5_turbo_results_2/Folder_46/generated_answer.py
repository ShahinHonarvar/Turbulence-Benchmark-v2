from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    anagram_pairs = 0
    for string in lst:
        counter[tuple(Counter(string.lower()).items())] += 1
    for count in counter.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 38