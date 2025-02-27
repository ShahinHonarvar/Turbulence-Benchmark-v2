def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i in range(5, 7) and 'G' <= char <= 'p':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)