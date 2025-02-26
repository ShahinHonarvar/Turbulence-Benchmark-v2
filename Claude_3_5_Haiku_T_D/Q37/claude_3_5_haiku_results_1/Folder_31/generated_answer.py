def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 57 <= i <= 96 and '<' <= char <= 'w':
            result += ''.join((c for c in s if c != char))
        else:
            result = s
    return result or s