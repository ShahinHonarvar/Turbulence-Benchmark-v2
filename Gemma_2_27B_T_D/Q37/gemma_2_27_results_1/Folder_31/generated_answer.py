def filter_chars(s):
    result = []
    for c in s:
        if 57 <= ord(c) <= 96 and '<' <= c <= 'w':
            continue
        result.append(c)
    return ''.join(result)