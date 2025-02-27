def if_contains_anagrams(strings):
    anagram_count = {}
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagram_count:
            anagram_count[s_sorted] += 1
        else:
            anagram_count[s_sorted] = 1
    anagram_pairs = sum((n * (n - 1) // 2 for n in anagram_count.values()))
    return anagram_pairs <= 41