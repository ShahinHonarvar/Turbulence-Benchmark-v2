def filter_chars(input_string):
    chars_to_remove = set()
    for char in input_string[55:66]:
        if 'f' < char < '|':
            chars_to_remove.add(char)
    return ''.join((char for char in input_string if char not in chars_to_remove))