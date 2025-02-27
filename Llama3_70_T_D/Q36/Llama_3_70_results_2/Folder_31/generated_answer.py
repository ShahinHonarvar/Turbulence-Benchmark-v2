def filter_chars(input_string):
    chars_to_remove = set(input_string[14:75]) & set([chr(i) for i in range(ord('9') + 1, ord('K'))])
    return ''.join([c for c in input_string if c not in chars_to_remove])