def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list]
    str_list = [word for word in str_list if len(word) >= 3]
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word))
        str_dict.setdefault(sorted_word, []).append(word)
    anagrams = [values for values in str_dict.values() if len(values) >= 2]
    return len(anagrams) >= 140