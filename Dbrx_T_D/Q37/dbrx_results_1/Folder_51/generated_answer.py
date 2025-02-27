def filter_chars(input_string):
    chars_to_filter = set(input_string[36:41])
    chars_to_filter = {c for c in chars_to_filter if 'H' <= c <= 'e'}
    result = ''.join((c for c in input_string if c not in chars_to_filter))
    return result