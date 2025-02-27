def filter_chars(input_string):
    chars_to_remove = set(input_string[83:100])
    chars_to_remove = {c for c in chars_to_remove if ord(c) >= ord('*') and ord(c) <= ord('j')}
    result = ''.join((c for c in input_string if c not in chars_to_remove))
    return result