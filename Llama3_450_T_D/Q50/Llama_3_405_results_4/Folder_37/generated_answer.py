def if_contains_anagrams(strings):
    strings = [''.join(sorted(s.casefold())) for s in strings if len(s) >= 3]
    anagram_counts = {}
    for s in strings:
        if s in anagram_counts:
            anagram_counts[s] += 1
        else:
            anagram_counts[s] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs >= 29