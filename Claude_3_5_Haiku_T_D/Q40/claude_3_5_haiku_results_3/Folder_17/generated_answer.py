def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))[:11]
    return sorted_chars