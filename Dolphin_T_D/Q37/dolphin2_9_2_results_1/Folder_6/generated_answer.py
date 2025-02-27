def filter_chars(string):
    result = ''
    for i, char in enumerate(string):
        if 13 <= i <= 28 and 'c' <= char <= 'n':
            continue
        result += char
    return result