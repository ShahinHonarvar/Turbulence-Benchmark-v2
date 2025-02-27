def if_contains_anagrams(str_list):
    anagram_dict = {}
    for s in str_list:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s] += 1
                if anagram_dict[sorted_s] >= 246:
                    return True
            else:
                anagram_dict[sorted_s] = 1
    return False