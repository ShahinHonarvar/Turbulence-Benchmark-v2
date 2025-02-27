def return_n_smallest_chars(s):
    char_list = list(s)
    char_list.sort(key=lambda x: ord(x))
    return char_list[0:2][::-1]