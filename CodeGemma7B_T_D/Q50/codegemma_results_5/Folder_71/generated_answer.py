def if_contains_anagrams(str_list):
    str_dict = {}
    for str_ in str_list:
        str_ = str_.lower()
        sorted_str = ''.join(sorted(str_))
        if len(str_) >= 3 and sorted_str not in str_dict:
            str_dict[sorted_str] = [str_]
        elif len(str_) >= 3 and sorted_str in str_dict:
            str_dict[sorted_str].append(str_)
    anagram_count = 0
    for anagrams in str_dict.values():
        anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 57