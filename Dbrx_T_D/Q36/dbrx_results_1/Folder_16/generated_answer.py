def filter_chars(input_string):
    start_index = 331
    end_index = 713
    chars_to_remove = []
    for i in range(len(input_string)):
        if input_string[i] > 'M' and input_string[i] < '_':
            chars_to_remove.append(input_string[i])
    for char in chars_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string[start_index:end_index]