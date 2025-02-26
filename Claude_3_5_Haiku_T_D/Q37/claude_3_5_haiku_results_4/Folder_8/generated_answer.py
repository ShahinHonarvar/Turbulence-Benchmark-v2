def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 41 <= i <= 86 and 'S' <= char <= 's':
            result.extend([c for c in s if c != char])
            return ''.join(result)
    return s