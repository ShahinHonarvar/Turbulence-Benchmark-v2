def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 43 <= i <= 80 and '=' <= char <= 'E':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)