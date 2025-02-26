def return_n_smallest_chars(string):
    sorted_chars = sorted(list(set(string)))[:10]
    return sorted_chars