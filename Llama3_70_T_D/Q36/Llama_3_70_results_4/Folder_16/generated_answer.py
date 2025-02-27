def filter_chars(input_string):
    chars_to_remove = [char for idx, char in enumerate(input_string[331:713]) if 'M' < char < '_']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string