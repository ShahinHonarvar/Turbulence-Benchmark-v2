def if_contains_anagrams(str_list):
    str_dict = {}
    for str in str_list:
        new_str = ''.join(sorted(str.lower()))
        str_dict.setdefault(new_str, []).append(str)
    anagrams_count = 0
    for anagram_list in str_dict.values():
        pairs_count = len(anagram_list) * (len(anagram_list) - 1) // 2
        anagrams_count += pairs_count
    return anagrams_count <= 60