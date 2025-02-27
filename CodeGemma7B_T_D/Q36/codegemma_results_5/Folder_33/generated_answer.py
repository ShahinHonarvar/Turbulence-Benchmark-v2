def filter_chars(text):
    result = ''
    for i, char in enumerate(text):
        if i >= 299 and i < 418 and (char > '9') and (char < 'P'):
            continue
        result += char
    return result