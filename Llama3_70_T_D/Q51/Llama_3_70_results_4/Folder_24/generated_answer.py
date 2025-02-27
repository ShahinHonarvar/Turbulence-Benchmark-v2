def if_contains_anagrams(lst):
    lst_lower = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3 and s.isalpha()]
    anagram_counts = {}
    for s in lst_lower:
        if s in anagram_counts:
            anagram_counts[s] += 1
        else:
            anagram_counts[s] = 1
    anagram_pairs = 0
    for count in anagram_counts.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 96