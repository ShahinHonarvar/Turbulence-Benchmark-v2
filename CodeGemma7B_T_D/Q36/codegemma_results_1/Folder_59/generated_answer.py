def filter_chars(string):
    filtered_string = []
    for i in range(3, 8):
        if string[i] > '?' and string[i] < 'k':
            filtered_string.append(string[i])
    return ''.join(filtered_string)