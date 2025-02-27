def filter_chars(input_string):
    return ''.join((character for character in input_string[220:418] if not ('-' < character < 'v' and character in input_string)))