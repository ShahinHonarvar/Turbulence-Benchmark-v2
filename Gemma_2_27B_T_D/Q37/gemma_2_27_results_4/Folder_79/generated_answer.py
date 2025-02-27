def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i >= 10 and i <= 52 and (char >= '@') and (char <= 'T'):
            continue
        result.append(char)
    return ''.join(result)