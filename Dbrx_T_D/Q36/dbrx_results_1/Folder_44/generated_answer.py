def filter_chars(input_string):
    start_index = 18
    end_index = 64
    chars_to_remove = set(input_string[start_index:end_index])
    chars_to_remove = {c for c in chars_to_remove if '3' < c < 'B'}
    result = ''.join((c for c in input_string if c not in chars_to_remove))
    return result