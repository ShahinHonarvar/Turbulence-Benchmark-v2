def filter_chars(string):
    lower = string[73:75 + 1]
    filtered_string = ''
    for char in string:
        if char not in lower:
            filtered_string += char
    return filtered_string