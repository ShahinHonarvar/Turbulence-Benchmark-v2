def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_nine = sorted_chars[:9]
    return sorted(smallest_nine, reverse=True)