def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(41, 63):
        if i < len(input_string) and '7' < input_string[i] < 'H':
            chars_to_remove.add(input_string[i])
    return ''.join((char for char in input_string if char not in chars_to_remove))