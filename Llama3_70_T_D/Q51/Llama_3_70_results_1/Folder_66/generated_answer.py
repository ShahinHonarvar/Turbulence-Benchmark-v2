def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        s_sorted = ''.join(sorted((c for c in s_lower if c.isalpha())))
        if len(s_sorted) < 3:
            continue
        if s_sorted in anagrams:
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return anagram_pairs <= 64