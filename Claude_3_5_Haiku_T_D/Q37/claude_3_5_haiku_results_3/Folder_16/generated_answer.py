def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 225 <= i <= 381 and 'D' <= char <= 'Y':
            continue
        result += char
    return result