def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s_lower = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s_lower)
        else:
            anagram_dict[sorted_s] = [s_lower]
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_count >= 233