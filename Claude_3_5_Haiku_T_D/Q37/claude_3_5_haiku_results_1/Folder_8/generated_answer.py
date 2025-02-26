def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 41 <= i <= 86 and 'S' <= char <= 's':
            result.append(char)
    return ''.join((char for char in s if char not in result))