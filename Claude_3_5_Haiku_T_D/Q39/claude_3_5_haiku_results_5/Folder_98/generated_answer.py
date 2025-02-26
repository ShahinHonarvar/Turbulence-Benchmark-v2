def return_n_greatest_chars(string):
    unique_chars = sorted(set(string), reverse=True)
    return unique_chars[:68]