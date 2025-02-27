def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            sorted_s = ''.join(sorted(lower_s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(lower_s)
            else:
                anagram_dict[sorted_s] = [lower_s]
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
            if anagram_count > 98:
                return False
    return True