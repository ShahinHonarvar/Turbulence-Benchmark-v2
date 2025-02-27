def filter_chars(input_string):
    filtered_string = ''
    chars_to_remove = set(input_string[60:71])
    for char in input_string:
        if char < '0' or char > '@' or char not in chars_to_remove:
            filtered_string += char
    return filtered_string