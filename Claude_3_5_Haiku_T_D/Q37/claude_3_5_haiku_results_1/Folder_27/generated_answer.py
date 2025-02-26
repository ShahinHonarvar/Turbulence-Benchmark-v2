def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 43 <= i <= 80 and '=' <= char <= 'E':
            result.extend((c for c in s if c != char))
            return ''.join(result)
    return s