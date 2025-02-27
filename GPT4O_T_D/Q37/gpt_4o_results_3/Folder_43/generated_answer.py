def filter_chars(input_string):
    chars_to_remove = set(input_string[15:56])
    filtered_chars = {c for c in chars_to_remove if 'W' <= c <= '{'}
    return ''.join((c for c in input_string if c not in filtered_chars))