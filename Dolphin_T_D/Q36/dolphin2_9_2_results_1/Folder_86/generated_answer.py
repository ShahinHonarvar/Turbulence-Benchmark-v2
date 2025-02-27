def filter_chars(string):
    new_string = ''
    for i in string:
        if i >= 'X' and i < '}':
            new_string += i
    return new_string