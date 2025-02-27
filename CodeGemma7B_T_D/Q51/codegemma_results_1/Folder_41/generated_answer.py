def if_contains_anagrams(str_list):
    str_dict = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        str_dict.setdefault(sorted_word, []).append(word)
    count = 0
    for values in str_dict.values():
        if len(values) > 1:
            count += len(values) // 2
    return count <= 52