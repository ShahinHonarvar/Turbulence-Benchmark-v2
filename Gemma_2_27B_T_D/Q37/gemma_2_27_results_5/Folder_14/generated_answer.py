def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 35 <= i <= 98 and 'A' <= char <= 'b':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)