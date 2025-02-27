def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 44 or i > 59:
            filtered_string += string[i]
        elif string[i] > '/' and string[i] < '6':
            filtered_string += ''
    return filtered_string