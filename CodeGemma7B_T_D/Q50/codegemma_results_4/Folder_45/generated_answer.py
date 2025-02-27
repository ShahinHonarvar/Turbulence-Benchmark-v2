def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list if len(word) >= 3]
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in str_dict:
            str_dict[sorted_word] += 1
        else:
            str_dict[sorted_word] = 1
    return max(str_dict.values()) >= 277