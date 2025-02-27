def filter_chars(input_string):
    chars_to_filter = set(input_string[515:539])
    input_string = ''.join((char for char in input_string if char < '+' or char > '}' or char not in chars_to_filter))
    return input_string