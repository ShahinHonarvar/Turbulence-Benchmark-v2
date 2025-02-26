def filter_chars(input_str):
    chars_to_remove = set()
    for i in range(32, 50):
        if '/' < input_str[i] < 'J':
            chars_to_remove.add(input_str[i])
    result = ''.join((char for char in input_str if char not in chars_to_remove))
    return result