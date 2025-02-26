def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    smallest_43 = sorted_chars[:43]
    return sorted(smallest_43, reverse=True)