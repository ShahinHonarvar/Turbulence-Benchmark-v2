def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if 63 <= i < 89 and string[i] > '*' and (string[i] < 'w'):
            new_string += string.replace(string[i], '')
        else:
            new_string += string[i]
    return new_string