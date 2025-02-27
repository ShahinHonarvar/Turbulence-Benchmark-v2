def return_n_smallest_chars(str):
    sorted_chars = sorted(set(str), key=ord)
    return sorted_chars[:38]