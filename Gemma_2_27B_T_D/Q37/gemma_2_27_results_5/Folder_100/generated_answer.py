def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (88 <= i <= 90 and 'J' <= char <= 'Q'):
            result.append(char)
    return ''.join(result)