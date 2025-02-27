def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i >= 20 and i <= 79 and (char >= '!') and (char <= 'T'):
            continue
        result.append(char)
    return ''.join(result)