def filter_chars(input_string):
    chars_to_remove = [shutil.copy(c) for c in input_string[35:60] if '!' < c < 'B']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string