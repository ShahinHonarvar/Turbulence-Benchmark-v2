from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    substrings = []
    for string in strings:
        if len(string) >= 3:
            substrings.append(string)
    anagram_counts = Counter()
    for s in substrings:
        sorted_tuple = tuple(sorted(s))
        anagram_counts[sorted_tuple] += 1
    pairs_count = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
    return pairs_count <= 14