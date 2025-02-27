def filter_chars(s: str) -> str:
    result = []
    for i, c in enumerate(s):
        if 331 < i < 713 and 'M' < c < '_':
            continue
        result.append(c)
    return ''.join(result)