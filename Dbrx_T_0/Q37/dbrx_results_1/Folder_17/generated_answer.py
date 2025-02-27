def filter_chars(input_string):
    chars_to_remove = set(input_string[27:30])
    chars_to_remove = {c for c in chars_to_remove if ord(';') <= ord(c) <= ord('b')}
    result = ''.join((c for c in input_string if c not in chars_to_remove))
    return result