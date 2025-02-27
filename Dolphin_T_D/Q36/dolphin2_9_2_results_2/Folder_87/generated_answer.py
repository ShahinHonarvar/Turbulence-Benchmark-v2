def filter_chars(input_string):
    chars_to_remove = [chr(i) for i in range(32, 61) if chr(i) > '3' and chr(i) < 'D']
    return ''.join((char for char in input_string if char not in chars_to_remove))