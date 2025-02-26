def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_six = sorted_chars[:6]
    return sorted(smallest_six, reverse=True)