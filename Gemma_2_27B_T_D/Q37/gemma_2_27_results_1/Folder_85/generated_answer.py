def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 28 <= i <= 65 and 'O' <= char <= 'd':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)