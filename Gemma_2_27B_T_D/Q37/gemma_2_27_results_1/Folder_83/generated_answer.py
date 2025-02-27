def filter_chars(s):
    result = []
    for i, ch in enumerate(s):
        if not (29 <= i <= 79 and 'K' <= ch <= 'z'):
            result.append(ch)
    return ''.join(result)