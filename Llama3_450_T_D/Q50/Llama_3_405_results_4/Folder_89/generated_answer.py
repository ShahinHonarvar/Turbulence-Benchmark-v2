def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s] += 1
        else:
            anagram_dict[sorted_s] = 1
    pairs = sum([n * (n - 1) // 2 for n in anagram_dict.values() if n > 1])
    return pairs >= 36