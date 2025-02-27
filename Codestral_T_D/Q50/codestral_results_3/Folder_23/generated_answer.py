def if_contains_anagrams(str_list):
    anagram_count = 0
    anagram_dict = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_s in anagram_dict:
                anagram_count += anagram_dict[sorted_s]
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    return anagram_count >= 67