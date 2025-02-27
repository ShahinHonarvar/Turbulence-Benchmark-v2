def return_n_greatest_chars(s):
    char_list = list(s)
    sorted_chars = sorted(char_list, key=lambda c: -ord(c))
    return sorted_chars[:72]