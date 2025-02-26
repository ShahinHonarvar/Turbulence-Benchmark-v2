def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 12 <= i <= 77 and ':' <= char <= 'L':
            result.append(''.join((c for c in s if c != char)))
            return result[0]
    return s