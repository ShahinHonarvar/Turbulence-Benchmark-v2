def if_contains_anagrams(strings):
    anagram_counts = {}
    for s in strings:
        if len(s) < 3:
            continue
        s = ''.join(sorted(s.lower()))
        if s in anagram_counts:
            anagram_counts[s] += 1
        else:
            anagram_counts[s] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 43