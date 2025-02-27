def filter_chars(s):
    result = ''
    for c in s:
        if not (26 <= s.index(c) <= 64 and 'V' <= c <= 'o'):
            result += c
    return result