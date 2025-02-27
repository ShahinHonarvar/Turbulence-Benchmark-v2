def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 12 <= i <= 88 and '&' <= char <= 'v':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)