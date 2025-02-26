def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 13 <= i <= 28 and 'c' <= char <= 'n':
            result.append(char)
    return ''.join((char for char in s if char not in result))