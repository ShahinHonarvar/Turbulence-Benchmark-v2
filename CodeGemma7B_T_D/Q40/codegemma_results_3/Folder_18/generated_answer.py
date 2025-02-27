def return_n_smallest_chars(string):
    ascii_values = sorted([ord(char) for char in string])
    return ascii_values[:52]