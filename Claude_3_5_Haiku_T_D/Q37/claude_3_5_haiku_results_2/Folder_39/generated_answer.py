def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 52 <= i <= 81 and 'A' <= char <= 'U':
            result.append(char)
    filtered = ''.join((char for char in s if char not in result))
    return filtered