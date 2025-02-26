def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(53, 88):
        if '&' < input_string[i] < 'c':
            chars_to_remove.add(input_string[i])
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result