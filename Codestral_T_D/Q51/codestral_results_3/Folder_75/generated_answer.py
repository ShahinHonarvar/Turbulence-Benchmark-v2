def if_contains_anagrams(str_list):
    anagram_count = 0
    str_dict = {}
    for s in str_list:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in str_dict:
                str_dict[sorted_s] += 1
            else:
                str_dict[sorted_s] = 1
    for count in str_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 55