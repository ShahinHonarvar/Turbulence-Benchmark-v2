def return_n_smallest_chars(string_of_chars):
    list_of_chars = sorted(list(string_of_chars), key=ord)
    return list_of_chars[:52]