def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 35 <= i <= 98 and 'A' <= char <= 'b':
            result.extend([c for c in s if c != char])
            return ''.join(result)
    return s