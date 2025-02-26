def return_n_smallest_chars(string):
    sorted_chars = sorted(list(set(string)))[:21]
    return sorted(sorted_chars, reverse=True)