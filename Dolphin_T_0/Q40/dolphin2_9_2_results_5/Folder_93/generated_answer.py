def return_n_smallest_chars(s):
    sorted_chars = [char for char in s]
    sorted_chars.sort(key=ord, reverse=True)
    return sorted_chars[:77]