def return_n_smallest_chars(s):
    list_chars = list(s)
    list_chars.sort(reverse=True)
    return list_chars[:90]