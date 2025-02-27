def return_n_smallest_chars(str_of_unique_chars):
    list_of_unique_chars = list(str_of_unique_chars)
    list_of_unique_chars.sort(key=ord, reverse=True)
    return list_of_unique_chars[:48]