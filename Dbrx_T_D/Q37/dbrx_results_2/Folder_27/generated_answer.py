def filter_chars(input_string):
    chars_to_filter = [char for char in input_string[43:81] if '==' <= char <= 'E']
    for char in chars_to_filter:
        input_string = input_string.replace(char, '')
    return input_string