def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[502:946] if 'W' < char < 'y']
    filtered_string = ''.join([char for char in input_string if char not in chars_to_remove])
    return filtered_string