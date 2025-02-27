def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = 0
    freq_map = {}
    for s in sorted_strings:
        if s in freq_map:
            anagram_count += freq_map[s]
            freq_map[s] += 1
        else:
            freq_map[s] = 1
    return anagram_count >= 411