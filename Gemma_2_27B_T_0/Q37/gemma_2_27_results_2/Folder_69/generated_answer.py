def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (114 <= i <= 639 and '!' <= char <= 'x'):
            result.append(char)
    return ''.join(result)