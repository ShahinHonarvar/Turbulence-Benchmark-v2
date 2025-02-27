def return_n_smallest_chars(s):
    ascii_values = [ord(c) for c in s]
    ascii_values.sort(reverse=True)
    n_smallest_chars = [chr(i) for i in ascii_values[:44]]
    return n_smallest_chars