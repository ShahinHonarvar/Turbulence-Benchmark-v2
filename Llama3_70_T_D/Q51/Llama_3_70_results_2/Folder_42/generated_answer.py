def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s] = anagrams.get(sorted_s, 0) + 1
    anagram_pairs = sum([count * (count - 1) // 2 for count in anagrams.values()])
    return anagram_pairs <= 38