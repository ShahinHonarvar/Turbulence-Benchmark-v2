def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 672 and i <= 709 and (char > 'X') and (char < '}'):
            continue
        filtered_string += char
    return filtered_string