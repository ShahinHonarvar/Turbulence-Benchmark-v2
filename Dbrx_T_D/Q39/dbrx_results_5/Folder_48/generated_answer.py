def return_n_greatest_chars(string):
    sorted_chars = sorted(list(set(string)))
    return sorted_chars[-12:]