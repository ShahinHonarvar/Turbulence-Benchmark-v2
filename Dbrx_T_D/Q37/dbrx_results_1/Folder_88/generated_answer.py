def filter_chars(input_string):
    chars_to_remove = set(input_string[69:81])
    chars_to_remove = {c for c in chars_to_remove if ord(c) <= ord('p') and ord(c) >= ord('@')}
    result = ''.join((c for c in input_string if c not in chars_to_remove))
    return result