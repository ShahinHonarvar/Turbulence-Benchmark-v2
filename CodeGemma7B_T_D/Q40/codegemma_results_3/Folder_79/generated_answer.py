def return_n_smallest_chars(str):
    return sorted(set(str), key=ord, reverse=True)[:82]