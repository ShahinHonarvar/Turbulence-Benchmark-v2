def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i > 1 and i < 9 and (string[i] > '8') and (string[i] < 'm'):
            continue
        else:
            new_string += string[i]
    return new_string