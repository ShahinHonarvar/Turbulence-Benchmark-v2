def filter_chars(input_string):
    filtered_string = ''
    for i, char in enumerate(input_string):
        if i >= 503 and i <= 753 and (char >= '9') and (char <= 'w'):
            continue
        filtered_string += char
    return filtered_string