def filter_chars(input_str):
    chars_to_remove = set()
    for i in range(319, 337):
        if 'B' < input_str[i] < 'z':
            chars_to_remove.add(input_str[i])
    result = ''.join((char for char in input_str if char not in chars_to_remove))
    return result