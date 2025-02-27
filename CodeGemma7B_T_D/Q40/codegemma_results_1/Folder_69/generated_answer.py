def return_n_smallest_chars(str):
    list = list(str)
    list.sort(key=ord, reverse=True)
    return list[:65]