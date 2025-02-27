def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 40 or i >= 63:
            filtered_string += string[i]
        elif string[i] > '7' and string[i] < 'H':
            filtered_string += string[i].replace(string[i], '')
        else:
            filtered_string += string[i]
    return filtered_string