def return_n_greatest_chars(str_of_chars):
    list_of_chars = list(str_of_chars)
    list_of_chars.sort(key=ord, reverse=True)
    return list_of_chars[:64]