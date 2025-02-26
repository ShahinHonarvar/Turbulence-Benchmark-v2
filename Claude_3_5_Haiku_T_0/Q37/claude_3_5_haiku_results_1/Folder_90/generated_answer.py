def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 348 <= i <= 852 and 'J' <= char <= 'b':
            result.append(char)
    return ''.join(result)