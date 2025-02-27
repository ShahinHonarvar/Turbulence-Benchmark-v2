def return_n_smallest_chars(chars):
    return sorted(sorted(chars), key=ord, reverse=True)[:90]