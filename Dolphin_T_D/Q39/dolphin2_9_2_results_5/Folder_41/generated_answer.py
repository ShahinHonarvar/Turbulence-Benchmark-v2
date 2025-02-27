def return_n_greatest_chars(input_string):
    chars = max(input_string, key=lambda x: ord(x))
    return ''.join(sorted(chars))