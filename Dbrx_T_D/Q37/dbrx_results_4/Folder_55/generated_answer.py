def filter_chars(input_string):
    chars_to_filter = set(input_string[1:6])
    chars_to_filter = {c for c in chars_to_filter if '$' <= c <= ';'}
    return ''.join((c for c in input_string if c not in chars_to_filter))