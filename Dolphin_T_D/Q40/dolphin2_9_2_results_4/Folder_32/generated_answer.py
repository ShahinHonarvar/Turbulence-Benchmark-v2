def return_n_smallest_chars(input_string):
    s = sorted(input_string, key=lambda x: ord(x))
    return s[:8]