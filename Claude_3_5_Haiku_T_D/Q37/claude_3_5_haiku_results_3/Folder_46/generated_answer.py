def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 11 <= i <= 72 and 'i' <= char <= 'v':
            result.append(char)
    filtered = ''.join((c for c in s if c not in result))
    return filtered