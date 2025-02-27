def return_n_smallest_chars(string):
    characters = sorted(list(set(string)))[:14]
    return characters