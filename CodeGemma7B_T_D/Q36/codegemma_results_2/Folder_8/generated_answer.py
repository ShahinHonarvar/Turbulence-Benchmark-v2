def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i < 82 or i >= 93:
            new_string += string[i]
        elif string[i] > '!' and string[i] < '*':
            continue
        else:
            new_string += string[i]
    return new_string