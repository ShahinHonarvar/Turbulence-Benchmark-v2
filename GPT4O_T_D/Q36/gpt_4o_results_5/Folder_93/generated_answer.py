def filter_chars(input_string):
    if len(input_string) < 89:
        return input_string
    target_section = input_string[53:88]
    chars_to_remove = {char for char in target_section if '&' < char < 'c'}
    return ''.join((char for char in input_string if char not in chars_to_remove))