def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))[:35]
    return sorted(sorted_chars, reverse=True)