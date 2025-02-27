def filter_chars(s: str) -> str:
    chars_to_remove = set(s[39:87])
    filtered_chars = [c for c in s if c < '!' or c > '}' or c not in chars_to_remove]
    return ''.join(filtered_chars)