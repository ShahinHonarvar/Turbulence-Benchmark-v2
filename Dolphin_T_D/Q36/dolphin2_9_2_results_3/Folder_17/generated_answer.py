def filter_chars(input_string):
    chars_to_filter = []
    for i in range(18, 95):
        if 'K' < input_string[i] < 'a':
            chars_to_filter.append(input_string[i])
    for char in chars_to_filter:
        input_string = input_string.replace(char, '')
    return input_string