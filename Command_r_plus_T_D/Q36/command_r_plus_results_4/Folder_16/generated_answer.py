def filter_chars(s: str) -> str:
    result = []
    to_remove = set()
    for i, c in enumerate(s, 1):
        if 331 < i < 713 and 'M' < c < '_':
            to_remove.add(c)
    for c in s:
        if c not in to_remove:
            result.append(c)
    return ''.join(result)