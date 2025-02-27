def filter_chars(string):
    indices_range = range(31, 39)
    chars_to_filter = [c for c in string if ord(c) >= ord(';') and ord(c) <= ord('g') and (string.index(c) in indices_range)]
    new_string = [c for c in string if c not in chars_to_filter]
    return ''.join(new_string)