def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if i >= 722 and i <= 832 and (char >= 'K') and (char <= 'm'):
            continue
        result += char
    return result