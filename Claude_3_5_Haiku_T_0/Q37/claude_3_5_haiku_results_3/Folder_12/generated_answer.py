def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 19 <= i <= 90 and 'F' <= char <= 'h':
            result.append(char)
    return ''.join((char for char in s if char not in result))