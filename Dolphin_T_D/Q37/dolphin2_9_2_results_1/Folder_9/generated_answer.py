def filter_chars(s):
    result = ''
    to_remove = set()
    for i, c in enumerate(s):
        if 38 <= i <= 99 and 'A' <= c <= 'Q':
            to_remove.add(c)
    for c in s:
        if c not in to_remove:
            result += c
    return result