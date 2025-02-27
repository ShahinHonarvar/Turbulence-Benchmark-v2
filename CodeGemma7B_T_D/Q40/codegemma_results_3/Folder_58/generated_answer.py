def return_n_smallest_chars(str_of_chars):
    list_of_chars = list(str_of_chars)
    list_of_chars.sort(key=lambda x: ord(x), reverse=True)
    return list_of_chars[:49]