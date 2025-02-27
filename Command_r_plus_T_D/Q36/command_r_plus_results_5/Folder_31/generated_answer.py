def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[14:75] if '9' < c < 'K']
    result = []
    for c in s:
        if c in chars_to_remove:
            continue
        result.append(c)
    return ''.join(result)