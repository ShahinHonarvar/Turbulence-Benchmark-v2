def filter_chars(string):
    new_str = ''
    for i in range(len(string)):
        if i < 2 or i >= 7:
            new_str += string[i]
        elif string[i] <= 'h' or string[i] >= 'k':
            continue
        else:
            new_str += string[i]
    return new_str