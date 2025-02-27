def if_contains_anagrams(str_list):
    str_list = [x.lower() for x in str_list]
    str_list = [x for x in str_list if len(x) >= 3]
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in str_dict:
            str_dict[sorted_word] += 1
        else:
            str_dict[sorted_word] = 1
    return sum((v ** 2 for v in str_dict.values())) <= 445 ** 2