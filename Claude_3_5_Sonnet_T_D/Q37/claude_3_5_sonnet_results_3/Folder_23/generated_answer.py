def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(51, 78):
        if i < len(input_string):
            if 'V' <= input_string[i] <= 'Y':
                chars_to_remove.add(input_string[i])
    return ''.join((char for char in input_string if char not in chars_to_remove))