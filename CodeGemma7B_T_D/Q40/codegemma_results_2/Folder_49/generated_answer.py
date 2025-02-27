def return_n_smallest_chars(str):
    char_asc_list = [(char, ord(char)) for char in str]
    char_asc_list.sort(key=lambda pair: pair[1], reverse=True)
    return [char for char, _ in char_asc_list[:76]]