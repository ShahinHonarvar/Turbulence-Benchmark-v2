def filter_chars(str):
    filtered_str = str
    for i in range(1, 9):
        char = str[i]
        if char > '8' and char < 'm':
            filtered_str = filtered_str.replace(char, '')
    return filtered_str