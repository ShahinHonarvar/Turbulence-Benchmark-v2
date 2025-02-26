def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 29 <= i <= 97 and '-' <= char <= 'n':
            continue
        result += char
    return result