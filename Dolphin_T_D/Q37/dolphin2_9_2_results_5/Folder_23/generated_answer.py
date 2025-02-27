def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 51 <= i <= 77 and 'V' <= c <= 'Y':
            continue
        result += c
    return result