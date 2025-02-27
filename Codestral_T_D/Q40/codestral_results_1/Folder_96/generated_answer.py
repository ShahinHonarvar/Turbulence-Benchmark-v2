def return_n_smallest_chars(string):
    sorted_chars = sorted(string)[:20]
    sorted_chars.reverse()
    return sorted_chars