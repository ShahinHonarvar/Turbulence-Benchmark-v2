def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(s_lower)
        else:
            anagram_dict[sorted_str] = [s_lower]
    count = sum((len(val) * (len(val) - 1) // 2 for val in anagram_dict.values() if len(val) > 1))
    return count >= 35