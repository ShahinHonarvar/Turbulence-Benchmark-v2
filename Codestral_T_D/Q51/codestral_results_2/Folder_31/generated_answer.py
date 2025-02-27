def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    for key in anagram_dict:
        anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_count <= 65