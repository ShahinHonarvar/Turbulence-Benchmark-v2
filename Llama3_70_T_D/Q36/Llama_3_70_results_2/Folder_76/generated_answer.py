def filter_chars(input_string):
    chars_to_remove = set()
    for char in input_string[669:888]:
        if 'B' < char < 'Y':
            chars_to_remove.add(char)
    return ''.join([char for char in input_string if char not in chars_to_remove])