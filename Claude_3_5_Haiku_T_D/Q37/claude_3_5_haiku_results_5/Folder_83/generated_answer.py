def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 29 <= i <= 79 and 'K' <= char <= 'z':
            result.extend((c for c in s if c != char))
            return ''.join(result)
    return s