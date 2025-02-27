def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagram_dict:
            count += anagram_dict[sorted_str]
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1
    return count >= 123