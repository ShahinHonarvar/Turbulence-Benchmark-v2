def filter_chars(input_str):
    start_index = 283
    end_index = 484
    chars_to_remove = []
    for i in range(start_index, end_index):
        if 'l' < input_str[i] < 't':
            chars_to_remove.append(input_str[i])
    for char in chars_to_remove:
        input_str = input_str.replace(char, '', 1)
    return input_str