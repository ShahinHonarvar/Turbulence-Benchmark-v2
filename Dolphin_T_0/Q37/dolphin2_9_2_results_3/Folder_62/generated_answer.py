def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i < 10 or i > 69:
            new_string += string[i]
        elif string[i] < 'I' or string[i] > 'K':
            new_string += string[i]
    return new_string