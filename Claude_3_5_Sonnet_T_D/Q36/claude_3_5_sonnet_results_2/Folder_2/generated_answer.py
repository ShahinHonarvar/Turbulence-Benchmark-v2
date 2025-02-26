def filter_chars(input_string):
    result = list(input_string)
    chars_to_remove = set()
    for i in range(422, 854):
        if i < len(input_string) and 'D' < input_string[i] < 'J':
            chars_to_remove.add(input_string[i])
    return ''.join((char for char in result if char not in chars_to_remove))