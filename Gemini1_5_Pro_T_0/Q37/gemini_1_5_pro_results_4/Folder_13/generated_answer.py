def filter_chars(text):
    result = ''
    for i, char in enumerate(text):
        if not (124 <= i <= 854 and '9' <= char <= 's'):
            result += char
    return result