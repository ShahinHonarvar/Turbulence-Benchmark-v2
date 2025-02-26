def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 34 <= i <= 67 and 'W' <= char <= 'x':
            result.append(char)
    return ''.join((char for char in s if char not in result))