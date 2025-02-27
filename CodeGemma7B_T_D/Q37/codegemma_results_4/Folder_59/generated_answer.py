def filter_chars(str_input):
    filtered_str = ''
    for i, char in enumerate(str_input):
        if i >= 2 and i <= 3 and (char >= '5') and (char <= '_'):
            continue
        filtered_str += char
    return filtered_str