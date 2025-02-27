def return_n_smallest_chars(str):
    str = sorted(str, key=ord)
    return str[:49]