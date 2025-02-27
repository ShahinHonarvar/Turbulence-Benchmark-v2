def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i >= 23 and i <= 44 and (string[i] > '3') and (string[i] < 'I'):
            continue
        new_string += string[i]
    return new_string