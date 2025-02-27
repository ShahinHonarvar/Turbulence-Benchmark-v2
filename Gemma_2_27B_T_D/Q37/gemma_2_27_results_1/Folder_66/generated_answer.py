def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 27 <= i <= 85 and 'c' <= char <= 'i':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)