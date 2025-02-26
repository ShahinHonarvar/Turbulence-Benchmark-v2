def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 12 <= i <= 88 and '&' <= char <= 'v':
            result.append(char)
    return ''.join((char for char in s if char not in result))