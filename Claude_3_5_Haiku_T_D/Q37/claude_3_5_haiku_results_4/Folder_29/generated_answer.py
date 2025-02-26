def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 12 <= i <= 88 and '&' <= char <= 'v':
            result += ''.join((c for c in s if c != char))
            return result
    return s