def if_contains_anagrams(str_lst):
    str_dict = {}
    count = 0
    for word in str_lst:
        word = word.lower().replace(' ', '')
        sorted_word = ''.join(sorted(word))
        if sorted_word in str_dict:
            str_dict[sorted_word] += 1
            if str_dict[sorted_word] % 2 == 0:
                count += 1
        else:
            str_dict[sorted_word] = 1
    return count <= 73