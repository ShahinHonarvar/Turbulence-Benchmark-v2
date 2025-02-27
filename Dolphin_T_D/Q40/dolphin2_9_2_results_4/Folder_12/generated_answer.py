def return_n_smallest_chars(chars):
    sorted_chars = sorted(set(chars), key=lambda x: ord(x))
    return sorted_chars[:61]