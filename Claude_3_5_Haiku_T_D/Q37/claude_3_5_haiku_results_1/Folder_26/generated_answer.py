def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 20 <= i <= 62 and 'i' <= char <= 'k':
            result.append(char)
    return ''.join((c for c in s if c not in result))