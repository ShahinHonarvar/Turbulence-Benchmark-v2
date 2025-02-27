def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[512:878] if '?' <= c <= 'n']
    result = ''
    for c in s:
        if c not in chars_to_remove:
            result += c
    return result