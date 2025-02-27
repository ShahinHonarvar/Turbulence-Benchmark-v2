def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 35 or i > 51:
            filtered_string += string[i]
        elif string[i] >= 'H' and string[i] <= 's':
            continue
        else:
            filtered_string += string[i]
    return filtered_string