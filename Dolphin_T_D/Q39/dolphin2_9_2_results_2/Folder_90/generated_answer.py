def return_n_greatest_chars(chars):
    char_list = list(chars)
    sorted_list = sorted(char_list, reverse=True)
    return sorted_list[:24]