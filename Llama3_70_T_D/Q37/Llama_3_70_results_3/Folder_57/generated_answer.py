def filter_chars(s):
    result = ''
    for c in s:
        if not (27 <= ord(c) <= 85 and '!' <= c <= 'B'):
            result += c
    return result