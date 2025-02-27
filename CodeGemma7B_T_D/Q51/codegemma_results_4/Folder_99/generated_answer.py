def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and sorted_word not in str_dict:
            str_dict[sorted_word] = 1
        elif len(sorted_word) >= 3 and sorted_word in str_dict:
            str_dict[sorted_word] += 1
    return len(str_dict) <= 93