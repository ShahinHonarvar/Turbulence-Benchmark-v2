def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    smallest_six = sorted_chars[:6]
    return sorted(smallest_six, reverse=True)