def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 11 <= i <= 72 and 'i' <= char <= 'v':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)