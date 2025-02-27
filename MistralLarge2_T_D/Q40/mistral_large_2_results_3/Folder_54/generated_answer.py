def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_79_chars = sorted_chars[:79]
    return sorted(smallest_79_chars, reverse=True)