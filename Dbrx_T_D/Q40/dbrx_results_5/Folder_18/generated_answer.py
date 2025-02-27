def return_n_smallest_chars(s):
    ascii_values = sorted((ord(c) for c in s))
    return [chr(i) for i in ascii_values[:52]][::-1]