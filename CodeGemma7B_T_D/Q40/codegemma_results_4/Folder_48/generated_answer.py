def return_n_smallest_chars(str):
    list_str = list(str)
    list_str.sort(key=ord)
    return list_str[:12]