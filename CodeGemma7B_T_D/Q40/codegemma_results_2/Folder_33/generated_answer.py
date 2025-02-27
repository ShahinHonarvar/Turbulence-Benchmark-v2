def return_n_smallest_chars(string):
    ascii_values = [(c, ord(c)) for c in string]
    ascii_values.sort(key=lambda x: x[1])
    return [c for c, _ in ascii_values[:36]]