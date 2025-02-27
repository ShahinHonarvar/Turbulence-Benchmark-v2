def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 5 <= i <= 6 and 'G' <= char <= 'p':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)