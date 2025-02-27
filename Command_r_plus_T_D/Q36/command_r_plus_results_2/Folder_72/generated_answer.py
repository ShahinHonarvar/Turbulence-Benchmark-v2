def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[45:68] if 'W' < c < 'x']
    result = []
    for char in s:
        if char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)