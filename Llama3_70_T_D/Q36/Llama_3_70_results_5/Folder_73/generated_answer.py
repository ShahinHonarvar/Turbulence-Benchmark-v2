def filter_chars(s):
    result = ''
    for c in s:
        if not 66 < ord(c) < 90 or not '#' < c < 'T':
            result += c
    return result