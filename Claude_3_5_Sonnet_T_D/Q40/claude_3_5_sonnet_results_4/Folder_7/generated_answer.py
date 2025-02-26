def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:49]
    while len(char_list) < 49:
        char_list.append(chr(ord(max(char_list)) + 1))
    return char_list