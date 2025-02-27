def filter_chars(string):
    filtered_string = []
    for i in range(len(string)):
        if i not in range(57, 69):
            filtered_string.append(string[i])
    return ''.join(filtered_string)