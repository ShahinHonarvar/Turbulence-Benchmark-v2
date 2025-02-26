def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 25 <= i <= 97 and 'm' <= char <= 'w':
            continue
        result += char
    return result