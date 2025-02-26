def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 33 <= i <= 70 and '7' <= char <= 'k':
            result.append(char)
    return ''.join((char for char in s if char not in result))