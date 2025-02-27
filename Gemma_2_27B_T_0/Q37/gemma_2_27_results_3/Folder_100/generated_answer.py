def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 88 <= i <= 90 and 'J' <= char <= 'Q':
            s = s.replace(char, '')
        result.append(char)
    return ''.join(result)