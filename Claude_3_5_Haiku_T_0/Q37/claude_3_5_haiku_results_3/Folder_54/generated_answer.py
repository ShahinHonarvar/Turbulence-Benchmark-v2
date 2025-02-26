def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 46 <= i <= 85 and '-' <= char <= 'X':
            result.append(char)
    return ''.join((char for char in s if char not in result))