def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 38 <= i <= 99 and 'A' <= char <= 'Q':
            result += ''.join((c for c in s if c != char))
            return result
    return s