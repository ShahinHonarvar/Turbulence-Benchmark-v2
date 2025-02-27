def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if not (51 <= i <= 96 and 'X' <= c <= 'p'):
            result += c
    return result