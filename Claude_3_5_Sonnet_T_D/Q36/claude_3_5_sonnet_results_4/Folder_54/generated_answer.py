def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(19, 38):
        if i < len(input_string) and ')' < input_string[i] < 'P':
            chars_to_remove.add(input_string[i])
    return ''.join((char for char in input_string if char not in chars_to_remove))