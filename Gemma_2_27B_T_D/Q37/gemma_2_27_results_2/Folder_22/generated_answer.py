def filter_chars(s):
    result = []
    for c in s:
        if 33 <= ord(c) <= 70 and '7' <= c <= 'k':
            continue
        result.append(c)
    return ''.join(result)