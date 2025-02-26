def filter_chars(input_string):
    result = ''
    chars_to_remove = set()
    for i in range(48, 75):
        if i < len(input_string):
            if '6' < input_string[i] < '_':
                chars_to_remove.add(input_string[i])
    for char in input_string:
        if char not in chars_to_remove:
            result += char
    return result