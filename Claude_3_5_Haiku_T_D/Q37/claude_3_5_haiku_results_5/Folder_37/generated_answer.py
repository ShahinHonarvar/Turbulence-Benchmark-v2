def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 17 <= i <= 63 and 'O' <= char <= '^':
            result.append(char)
    filtered = ''.join((char for char in s if char not in result))
    return filtered