def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 36 <= i <= 79 and 'a' <= char <= 'i':
            result.extend((c for c in s if c != char))
            return ''.join(result)
    return s