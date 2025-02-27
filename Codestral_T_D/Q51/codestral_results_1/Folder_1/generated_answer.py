def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_counts[s] = anagram_counts.get(s, 0) + 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 30