def filter_chars(input_str):
    substring = input_str[283:484]
    chars_to_remove = set()
    for char in substring:
        if 'l' < char < 't':
            chars_to_remove.add(char)
    result = ''.join((char for char in input_str if char not in chars_to_remove))
    return result