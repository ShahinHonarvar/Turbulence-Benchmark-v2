def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(34, 37) if i > 34 and i < 65]
    return ''.join((c for c in s if c not in chars_to_remove))