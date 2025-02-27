def filter_chars(s):
    result = ''
    for c in s:
        if not (25 <= ord(c) <= 97 and 'm' <= c <= 'w'):
            result += c
    return result