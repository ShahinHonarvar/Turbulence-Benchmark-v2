def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 24 <= i <= 79 and 'a' <= char <= 'f':
            result.append(char)
    return ''.join((c for c in s if c not in result))