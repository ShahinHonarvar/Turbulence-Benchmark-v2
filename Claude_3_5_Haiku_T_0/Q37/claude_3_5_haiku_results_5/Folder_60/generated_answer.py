def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 12 <= i <= 77 and ':' <= char <= 'L':
            result.append(char)
    return ''.join((char for char in s if char not in result))