def filter_chars(input_string):
    chars_to_remove = set()
    for char in input_string[4:9]:
        if '*' < char < 'E':
            chars_to_remove.add(char)
    return ''.join((char for char in input_string if char not in chars_to_remove))