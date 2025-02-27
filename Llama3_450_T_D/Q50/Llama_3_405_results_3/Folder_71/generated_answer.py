def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_dict:
            count += anagram_dict[sorted_s]
            anagram_dict[sorted_s] += 1
        else:
            anagram_dict[sorted_s] = 1
    return count >= 57