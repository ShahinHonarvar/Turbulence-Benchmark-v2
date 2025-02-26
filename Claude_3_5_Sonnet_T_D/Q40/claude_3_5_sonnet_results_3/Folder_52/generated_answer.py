def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:68]
    return char_list if len(char_list) == 68 else char_list + [chr(i) for i in range(128) if chr(i) not in char_list][:68 - len(char_list)]