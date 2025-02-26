def return_n_smallest_chars(string):
    sorted_chars = sorted(string)[:76]
    return sorted(sorted_chars, reverse=True)