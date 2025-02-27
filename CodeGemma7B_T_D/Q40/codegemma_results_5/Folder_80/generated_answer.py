def return_n_smallest_chars(str):
    a = sorted(str, key=ord)
    return a[:35]