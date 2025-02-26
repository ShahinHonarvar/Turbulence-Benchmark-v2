def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_seven = sorted_chars[:7]
    return sorted(smallest_seven, reverse=True)