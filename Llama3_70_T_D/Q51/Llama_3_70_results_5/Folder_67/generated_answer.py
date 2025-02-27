def if_contains_anagrams(lst):
    anagram_dict = {}
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1
    anagram_count = sum((1 for v in anagram_dict.values() if v > 1))
    return anagram_count <= 5