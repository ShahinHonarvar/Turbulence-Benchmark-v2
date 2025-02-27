def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i not in range(4, 8):
            filtered_string += string[i]
    return filtered_string