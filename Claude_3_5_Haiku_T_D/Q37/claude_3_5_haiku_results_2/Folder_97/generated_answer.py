def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 227 <= i <= 235 and 'D' <= char <= 'u':
            result.append(char)
    return ''.join(result)