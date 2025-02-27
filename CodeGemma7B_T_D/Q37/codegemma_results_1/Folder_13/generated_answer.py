def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 124 and i <= 854 and (string[i] >= '9') and (string[i] <= 's'):
            filtered_string += ''
        else:
            filtered_string += string[i]
    return filtered_string