def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 35 <= i <= 89 and 'E' <= char <= 't':
            result += ''.join((c for c in s if c != char))
            break
    return result or s