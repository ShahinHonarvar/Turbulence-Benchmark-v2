def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 33 <= i <= 70 and '7' <= char <= 'k':
            result.append(char)
    return ''.join((c for c in s if c not in result))