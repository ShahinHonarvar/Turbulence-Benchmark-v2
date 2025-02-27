def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagram_dict:
                anagram_dict[sorted_s] = [s]
            else:
                anagram_dict[sorted_s].append(s)
    anagram_pairs = sum([len(l) * (len(l) - 1) // 2 for l in anagram_dict.values()])
    return anagram_pairs >= 411