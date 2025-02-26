def return_n_greatest_chars(string):
    unique_chars = sorted(set(string), reverse=True)[:36]
    return sorted(unique_chars)