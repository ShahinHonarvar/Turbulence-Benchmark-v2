def return_n_smallest_chars(str):
    unique_chars = list(set(str))
    unique_chars.sort(key=ord)
    return unique_chars[:85]