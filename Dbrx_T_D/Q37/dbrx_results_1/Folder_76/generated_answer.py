def filter_chars(input_string):
    filtered_string = ''
    chars_to_filter = set(input_string[379:899])
    for char in chars_to_filter:
        if 'M' <= char <= 'v':
            input_string = input_string.replace(char, '')
    for char in input_string:
        if not char.isspace():
            filtered_string += char
    return filtered_string