def return_n_smallest_chars(s):
    list_chars = list(s)
    list_chars.sort(key=ord)
    return list_chars[:47][::-1]