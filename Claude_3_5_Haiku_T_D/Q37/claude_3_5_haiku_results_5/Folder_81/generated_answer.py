def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 19 <= i <= 92 and '8' <= char <= 'm':
            result += ''.join((c for c in s if c != char))
            return result
    return s