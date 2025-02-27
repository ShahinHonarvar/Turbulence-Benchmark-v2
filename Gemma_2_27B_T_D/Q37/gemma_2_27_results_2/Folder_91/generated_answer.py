def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 7 <= i <= 8 and 'B' <= char <= 'H':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)