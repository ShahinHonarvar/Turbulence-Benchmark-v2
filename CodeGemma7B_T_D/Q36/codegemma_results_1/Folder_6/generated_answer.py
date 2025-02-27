def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i < 31 or i >= 70 or string[i] <= 'B' or (string[i] >= 'v'):
            new_string += string[i]
    return new_string