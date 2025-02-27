def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if not 25 <= i <= 97 or not 'm' <= char <= 'w':
            result += char
    return result