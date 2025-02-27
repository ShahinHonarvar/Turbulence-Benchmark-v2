def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return anagram_pairs <= 81