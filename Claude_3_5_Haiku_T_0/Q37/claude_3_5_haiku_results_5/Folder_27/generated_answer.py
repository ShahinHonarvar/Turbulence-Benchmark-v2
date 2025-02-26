def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 43 <= i <= 80 and '=' <= char <= 'E':
            result.append(char)
    return ''.join((char for char in s if char not in result))