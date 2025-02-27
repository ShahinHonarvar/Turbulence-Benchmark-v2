def filter_chars(input_string):
    chars_range = range(41, 87)
    chars_to_filter = ['S', 's']
    filtered_string = ''
    for i, char in enumerate(input_string):
        if i in chars_range and char in chars_to_filter:
            filtered_string += input_string.replace(char, '')
        else:
            filtered_string += char
    return filtered_string