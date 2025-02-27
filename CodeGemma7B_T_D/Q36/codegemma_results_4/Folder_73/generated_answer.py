def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i not in range(66, 90):
            filtered_string += char
    return filtered_string