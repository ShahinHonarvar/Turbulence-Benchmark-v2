def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 513 and i <= 877 and ('?' <= char <= 'n'):
            continue
        filtered_string += char
    return filtered_string