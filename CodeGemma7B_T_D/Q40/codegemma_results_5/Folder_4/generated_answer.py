def return_n_smallest_chars(str):
    return sorted(list(str), key=ord, reverse=True)[:90]