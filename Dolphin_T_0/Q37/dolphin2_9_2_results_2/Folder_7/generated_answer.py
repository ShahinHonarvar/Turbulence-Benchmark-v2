def filter_chars(string):
    new_string = ''
    for i, char in enumerate(string):
        if not (521 <= i <= 722 and char >= '>' >= '_'):
            new_string += char
    return new_string