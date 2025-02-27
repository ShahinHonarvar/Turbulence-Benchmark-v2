def filter_chars(input_string):
    chars_to_remove = set(input_string[70:74][::-1])
    chars_to_remove = {c for c in chars_to_remove if c > 'A' and c < 'U'}
    result = ''.join((c for c in input_string if c not in chars_to_remove))
    return result