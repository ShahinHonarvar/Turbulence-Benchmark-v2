def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if not (36 <= i <= 79 and '2' <= char <= 's'):
            result += char
    return result