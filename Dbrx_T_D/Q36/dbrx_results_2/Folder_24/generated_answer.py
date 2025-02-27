def filter_chars(input_string):
    start_index = 10
    end_index = 15
    chars_to_remove = [char for char in input_string[start_index:end_index] if 't' < char < 'v']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string