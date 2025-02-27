def filter_chars(input_string):
    allowed_chars = [char for char in input_string[8:10] if ord('R') <= ord(char) <= ord('t')]
    return ''.join((char for char in input_string if char not in allowed_chars))