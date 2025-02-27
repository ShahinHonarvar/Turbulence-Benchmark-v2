def filter_chars(string):
    new_str = ''
    for i in range(len(string)):
        if i >= 36 and i <= 79 and (string[i] >= 'a') and (string[i] <= 'i'):
            pass
        else:
            new_str += string[i]
    return new_str