def filter_chars(input_string):
    start_index = 318
    end_index = 337
    chars_to_remove = []
    for i in range(start_index, end_index):
        if 'B' < input_string[i] < 'z':
            chars_to_remove.append(input_string[i])
    for char in chars_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string