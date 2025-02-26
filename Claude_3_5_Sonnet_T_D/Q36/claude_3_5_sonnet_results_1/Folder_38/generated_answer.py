def filter_chars(input_string):
    chars_to_remove = set()
    for char in input_string[44:48]:
        if '+' < char < 'l':
            chars_to_remove.add(char)
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result