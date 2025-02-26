def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 225 <= i <= 381 and 'D' <= char <= 'Y':
            result += ''.join((c for c in s if c != char))
            break
    return result or s