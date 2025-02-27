def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    str_dict = {}
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s in str_dict:
            str_dict[sorted_s] += 1
        else:
            str_dict[sorted_s] = 1
    anagram_count = sum((count - 1 for count in str_dict.values() if count > 1))
    return anagram_count <= 289