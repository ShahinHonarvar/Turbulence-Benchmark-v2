def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_dict:
            if len(anagram_dict[sorted_s]) == 1:
                count += 1
            anagram_dict[sorted_s].append(s_lower)
        else:
            anagram_dict[sorted_s] = [s_lower]
    return count <= 279