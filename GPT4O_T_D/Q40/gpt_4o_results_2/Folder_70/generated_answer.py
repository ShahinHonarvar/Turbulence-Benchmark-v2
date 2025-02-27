def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_two = sorted_chars[:2]
    return sorted(smallest_two, reverse=True)