def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i >= 69 and i <= 80 and (char >= '@') and (char <= 'p'):
            continue
        result += char
    return result