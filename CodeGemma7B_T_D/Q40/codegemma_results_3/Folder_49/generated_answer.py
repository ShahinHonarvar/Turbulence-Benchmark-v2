def return_n_smallest_chars(str):
    list_of_chars = list(str)
    list_of_chars.sort(key=ord, reverse=False)
    return list_of_chars[:76]