def filter_chars(input_str):
    chars_to_remove = set()
    for i in range(42, 56):
        if 'Z' < input_str[i] < 'c':
            chars_to_remove.add(input_str[i])
    return ''.join((char for char in input_str if char not in chars_to_remove))