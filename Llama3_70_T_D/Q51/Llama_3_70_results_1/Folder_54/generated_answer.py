def if_contains_anagrams(strings):
    anagrams_count = {}
    for s in strings:
        s_lower = s.lower()
        s_filtered = ''.join(filter(str.isalpha, s_lower))
        if len(s_filtered) < 3:
            continue
        sorted_s = ''.join(sorted(s_filtered))
        if sorted_s in anagrams_count:
            anagrams_count[sorted_s] += 1
        else:
            anagrams_count[sorted_s] = 1
    anagrams_pairs = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return anagrams_pairs <= 39