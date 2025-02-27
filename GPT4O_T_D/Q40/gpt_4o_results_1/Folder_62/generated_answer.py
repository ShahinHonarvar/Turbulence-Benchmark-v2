def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_84 = sorted_chars[:84]
    return sorted(smallest_84, reverse=True)