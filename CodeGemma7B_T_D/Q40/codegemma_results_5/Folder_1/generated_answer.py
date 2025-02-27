def return_n_smallest_chars(s):
    ascii_values = sorted([ord(c) for c in s])[:11]
    return [chr(value) for value in ascii_values[::-1]]