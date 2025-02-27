def filter_chars(s):
    result = []
    for c in s:
        if c >= '!' and c <= '/' or (c >= ':' and c <= '@') or (c >= '[' and c <= '^'):
            continue
        result.append(c)
    return ''.join(result)