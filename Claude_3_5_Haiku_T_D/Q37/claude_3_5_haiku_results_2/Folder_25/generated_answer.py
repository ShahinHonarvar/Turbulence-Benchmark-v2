def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 31 <= i <= 38 and ';' <= char <= 'g':
            result += ''.join((c for c in s if c != char))
            break
    return result or s