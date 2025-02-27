def filter_chars(input_string):
    chars_to_filter = set(input_string[259:503])
    filter_chars = {chr(i) for i in range(ord(','), ord('3') + 1)}.intersection(chars_to_filter)
    result = ''.join((char for char in input_string if char not in filter_chars))
    return result