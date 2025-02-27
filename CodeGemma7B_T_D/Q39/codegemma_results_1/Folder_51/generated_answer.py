def return_n_greatest_chars(chars):
    char_list = list(chars)
    char_list.sort(key=ord, reverse=True)
    return char_list[:45]