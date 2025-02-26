def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(124, 855):
        if i < len(input_string):
            if '9' <= input_string[i] <= 's':
                chars_to_remove.add(input_string[i])
    return ''.join((char for char in input_string if char not in chars_to_remove))