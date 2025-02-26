def filter_chars(input_string):
    chars_to_remove = set()
    for char in input_string[5:8]:
        if '1' < char < 'J':
            chars_to_remove.add(char)
    return ''.join((char for char in input_string if char not in chars_to_remove))