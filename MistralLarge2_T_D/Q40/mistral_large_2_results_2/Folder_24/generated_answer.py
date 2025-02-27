def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_32_chars = sorted_chars[:32]
    return sorted(smallest_32_chars, reverse=True)