def if_contains_anagrams(str_list):
    anagrams_dict = {}
    for str in str_list:
        str = str.lower()
        str_sorted = ''.join(sorted(str))
        if len(str_sorted) >= 3:
            if str_sorted in anagrams_dict:
                anagrams_dict[str_sorted] += 1
            else:
                anagrams_dict[str_sorted] = 1
    pairs_count = 0
    for key in anagrams_dict.values():
        pairs_count += key * (key - 1) // 2
    return pairs_count <= 10