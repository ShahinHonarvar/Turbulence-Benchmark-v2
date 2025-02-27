def return_n_smallest_chars(s):
    ascii_values = list(map(ord, s))
    smallest_chars = ascii_values.copy()
    smallest_chars.sort()
    return [chr(smallest_chars[0]), chr(smallest_chars[1])]