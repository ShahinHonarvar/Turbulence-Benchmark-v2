def if_contains_anagrams(lst):
    anagram_dict = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s_lower)
            else:
                anagram_dict[sorted_s] = [s_lower]
    for v in anagram_dict.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 219