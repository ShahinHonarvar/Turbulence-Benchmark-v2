def filter_chars(text):
    filtered_string = ''
    for i in range(len(text)):
        char = text[i]
        if not (43 <= i <= 80 and '=' <= char <= 'E'):
            filtered_string += char
    return filtered_string