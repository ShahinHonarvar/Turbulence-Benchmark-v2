def filter_chars(text):
    result = ''
    for i, char in enumerate(text):
        if 124 <= i <= 854 and '9' <= char <= 's':
            result = result.replace(char, '')
        else:
            result += char
    return result