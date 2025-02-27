def return_n_greatest_chars(s):
    char_list = list(s)
    char_list.sort(reverse=True, key=lambda x: ord(x))
    return char_list[:72]