def if_contains_anagrams(str_list):
    str_list = [str_.lower() for str_ in str_list]
    str_list = [str_ for str_ in str_list if len(str_) >= 3]
    anagrams = {}
    for str_ in str_list:
        sorted_str = ''.join(sorted(str_))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(str_)
        else:
            anagrams[sorted_str] = [str_]
    return len(anagrams) >= 72