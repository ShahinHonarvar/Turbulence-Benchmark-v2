def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(310, 591):
        if 'S' < input_string[i] < 'm':
            chars_to_remove.add(input_string[i])
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result