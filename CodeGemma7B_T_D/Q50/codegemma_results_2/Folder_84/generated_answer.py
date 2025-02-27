def if_contains_anagrams(str_list):
    str_list.sort(key=len)
    str_freq_list = list(map(str_list.count, str_list))
    str_freq_dict = dict(zip(str_list, str_freq_list))
    num_anagrams = 0
    for key in str_freq_dict:
        if len(key) >= 3:
            num_anagrams += choose(str_freq_dict[key], 2)
    return num_anagrams >= 108