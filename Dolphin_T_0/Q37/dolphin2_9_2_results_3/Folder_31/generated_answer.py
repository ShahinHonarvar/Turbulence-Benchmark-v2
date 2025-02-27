def filter_chars(input_string):
    new_string = ''
    for i, char in enumerate(input_string):
        if i < 57 or i > 96:
            new_string += char
    return new_string