def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (114 <= i <= 639 and '!' <= char <= 'x'):
            result.append(char)
    return ''.join(result)