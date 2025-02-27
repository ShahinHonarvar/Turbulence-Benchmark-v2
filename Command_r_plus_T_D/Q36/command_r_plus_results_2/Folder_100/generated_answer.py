def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[43:69] if 'B' < c < 'r']
    result = []
    for c in s:
        if c in chars_to_remove:
            continue
        result.append(c)
    return ''.join(result)