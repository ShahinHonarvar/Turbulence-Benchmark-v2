def return_n_smallest_chars(string):
    smallest_chars = sorted(set(string))[:32]
    return smallest_chars