def return_n_smallest_chars(chars):
    return sorted(chars, key=ord)[:76][::-1]