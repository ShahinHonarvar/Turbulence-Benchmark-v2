def if_contains_anagrams(str_list):
    dict_list = []
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = sorted(word.lower())
        if sorted_word in dict_list:
            dict_list[sorted_word] += 1
            if max(dict_list.values()) - dict_list[sorted_word] > 11:
                return False
        else:
            dict_list[sorted_word] = 1
    return True