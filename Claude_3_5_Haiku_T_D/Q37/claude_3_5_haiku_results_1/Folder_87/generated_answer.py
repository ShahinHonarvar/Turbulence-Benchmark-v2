def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 18 <= i <= 81 and 'W' <= char <= '[':
            result.extend([c for c in s if c != char])
            return ''.join(result)
    return s