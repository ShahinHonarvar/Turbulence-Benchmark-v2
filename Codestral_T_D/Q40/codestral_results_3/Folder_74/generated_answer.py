def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    smallest_chars = sorted_chars[:5]
    return smallest_chars