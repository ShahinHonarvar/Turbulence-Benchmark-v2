def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 25 <= i <= 97 and 'm' <= char <= 'w':
            result.append(char)
    return ''.join((char for char in s if char not in result))