def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 4 and i <= 4 and (string[i] >= '7') and (string[i] <= 'o'):
            continue
        filtered_string += string[i]
    return filtered_string