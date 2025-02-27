def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i not in range(36, 80) or string[i] < '2' or string[i] > 's':
            filtered_string += string[i]
    return filtered_string