def filter_chars(input_string):
    start_index = 11
    end_index = 32
    for char_index in range(start_index, end_index + 1):
        char = input_string[char_index]
        if '!' <= char <= '@':
            input_string = input_string.replace(char, '', 1)
    return input_string