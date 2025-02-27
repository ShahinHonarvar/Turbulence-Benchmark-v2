def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 12 and i <= 77 and (char >= ':') and (char <= 'L'):
            pass
        else:
            filtered_string = filtered_string + char
    return filtered_string