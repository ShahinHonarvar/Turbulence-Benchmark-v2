def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i > 3 and i < 5 and (string[i] > 'Y') and (string[i] < 's'):
            continue
        else:
            new_string += string[i]
    return new_string