def return_n_smallest_chars(s):
    sorted_chars = sorted(s)[:79]
    return sorted(sorted_chars, reverse=True)