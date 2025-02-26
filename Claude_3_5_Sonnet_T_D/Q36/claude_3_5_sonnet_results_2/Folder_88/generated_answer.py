def filter_chars(input_string):
    chars_to_remove = [c for c in input_string[79:81] if 'S' < c < '[']
    return ''.join((c for c in input_string if c not in chars_to_remove))