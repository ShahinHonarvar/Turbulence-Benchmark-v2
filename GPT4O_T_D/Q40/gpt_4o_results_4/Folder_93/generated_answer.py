def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_77 = sorted_chars[:77]
    return sorted(smallest_77, reverse=True)