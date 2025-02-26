def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(515, 539):
        if i < len(input_string):
            if '+' <= input_string[i] <= '}':
                chars_to_remove.add(input_string[i])
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result