def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (15 <= i <= 55 and 'W' <= char <= '{'):
            result.append(char)
    return ''.join(result)