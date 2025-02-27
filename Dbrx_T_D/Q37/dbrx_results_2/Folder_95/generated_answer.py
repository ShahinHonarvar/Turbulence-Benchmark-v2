def filter_chars(input_string):
    chars_to_remove = {chr(i) for i in range(ord(')') + 1, ord('l') + 1)}
    return ''.join((char for char in input_string if char not in chars_to_remove))[35:40]