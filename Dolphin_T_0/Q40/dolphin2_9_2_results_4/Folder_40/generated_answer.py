def return_n_smallest_chars(string):
    return sorted([x for _, x in zip(range(7), string)])