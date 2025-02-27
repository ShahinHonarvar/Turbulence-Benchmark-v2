def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 35 or i >= 60 or (char <= '!' and char >= 'B'):
            filtered_string += char
    return filtered_string