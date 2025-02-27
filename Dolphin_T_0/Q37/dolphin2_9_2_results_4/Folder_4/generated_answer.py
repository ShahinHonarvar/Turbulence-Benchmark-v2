def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 19 <= i <= 33 and 'S' <= c <= '{':
            continue
        result += c
    return result