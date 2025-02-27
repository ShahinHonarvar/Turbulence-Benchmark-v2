def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            str_dict.setdefault(sorted_word, []).append(word)
    return len(str_dict) <= 21