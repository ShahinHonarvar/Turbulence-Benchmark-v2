def filter_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 20 <= i <= 79 and '!' <= c <= 'T':
            seen.add(c)
        elif c not in seen:
            result.append(c)
    return ''.join(result)