def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 81 or i > 89:
            filtered_string += string[i]
    return filtered_string