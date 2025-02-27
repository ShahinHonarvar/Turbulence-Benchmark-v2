def filter_chars(s):
    result = []
    for c in s:
        if not (32 <= ord(c) <= 46 and '0' <= c <= 'k'):
            result.append(c)
    return ''.join(result)