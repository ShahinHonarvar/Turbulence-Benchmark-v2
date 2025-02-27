def filter_chars(s):
    result = ''
    for c in s:
        if not (35 <= ord(c) <= 98 and 'A' <= c <= 'b'):
            result += c
    return result