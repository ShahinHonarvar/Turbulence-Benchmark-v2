def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))[:20]
    return sorted(sorted_chars, reverse=True)