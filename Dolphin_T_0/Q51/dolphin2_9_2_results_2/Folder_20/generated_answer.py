from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            counter[sorted_string] += 1
    pairs_of_anagrams = sum((c * (c - 1) // 2 for c in counter.values() if c > 1))
    return pairs_of_anagrams <= 131