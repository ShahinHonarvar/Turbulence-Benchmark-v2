def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 19 <= i <= 92 and '8' <= char <= 'm':
            result.append(char)
    return ''.join((char for char in s if char not in result))