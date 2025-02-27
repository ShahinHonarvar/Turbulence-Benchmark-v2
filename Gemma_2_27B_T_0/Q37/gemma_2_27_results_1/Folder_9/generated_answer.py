def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (38 <= i <= 99 and 'A' <= char <= 'Q'):
            result.append(char)
    return ''.join(result)