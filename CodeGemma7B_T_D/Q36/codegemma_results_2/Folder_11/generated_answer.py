def filter_chars(string):
    filtered_string = []
    index = 0
    for char in string:
        if index not in range(86, 93):
            filtered_string.append(char)
        index += 1
    return ''.join(filtered_string)