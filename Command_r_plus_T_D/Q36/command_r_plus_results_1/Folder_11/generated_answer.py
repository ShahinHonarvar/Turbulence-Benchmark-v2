def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[86:94] if 'E' < c < '~']
    result = []
    for c in s:
        if c in chars_to_remove:
            continue
        result.append(c)
    return ''.join(result)