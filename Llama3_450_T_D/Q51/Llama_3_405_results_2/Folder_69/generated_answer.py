def if_contains_anagrams(strings):
    strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_counts = {}
    for s in strings:
        anagram_counts[s] = anagram_counts.get(s, 0) + 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 58