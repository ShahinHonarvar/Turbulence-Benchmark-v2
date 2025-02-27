def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i >= 513 and i <= 877 and (char >= '?') and (char <= 'n'):
            continue
        else:
            result += char
    return result