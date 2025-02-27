def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (54 <= i <= 83 and 'j' <= char <= 'v'):
            result.append(char)
    return ''.join(result)