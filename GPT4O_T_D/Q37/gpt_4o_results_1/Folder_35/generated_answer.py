def filter_chars(s):
    if len(s) <= 403:
        return s
    to_remove = set()
    for i in range(155, 404):
        char = s[i]
        if '(' <= char <= ']':
            to_remove.add(char)
    result = ''.join((c for c in s if c not in to_remove))
    return result