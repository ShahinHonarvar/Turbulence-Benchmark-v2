def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 15 <= i <= 55 and 'W' <= char <= '{':
            result += ''.join((c for c in s if c != char))
            return result
    return s