def return_n_smallest_chars(string):
    sorted_chars = sorted(string)[:72]
    return sorted(sorted_chars, reverse=True)