def if_contains_anagrams(str_list):
    str_dict = {}
    for word in [word.lower() for word in str_list if len(word) >= 3]:
        sorted_word = ''.join(sorted(word))
        str_dict.setdefault(sorted_word, []).append(word)
    return len(str_dict) >= 52