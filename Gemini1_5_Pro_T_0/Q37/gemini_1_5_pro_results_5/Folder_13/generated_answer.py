def filter_chars(text):
    result = ''
    for i in range(len(text)):
        char = text[i]
        if not (124 <= i <= 854 and '9' <= char <= 's'):
            result += char
    return result