def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 28 <= i <= 65 and 'O' <= char <= 'd':
            result += ''.join((c for c in s if c != char))
            return result
    return s