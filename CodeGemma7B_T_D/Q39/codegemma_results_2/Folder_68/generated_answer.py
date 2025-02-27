def return_n_greatest_chars(str):
    char_list = sorted(str, key=ord, reverse=True)
    return char_list[:89]