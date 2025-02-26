def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(513, 878):
        if i < len(input_string):
            if '?' <= input_string[i] <= 'n':
                chars_to_remove.add(input_string[i])
    return ''.join((char for char in input_string if char not in chars_to_remove))