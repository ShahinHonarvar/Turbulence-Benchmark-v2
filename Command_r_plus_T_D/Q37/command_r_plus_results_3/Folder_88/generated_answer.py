def filter_chars(s: str) -> str:
    chars_to_remove = set(s[69:81]) & set('@ABCDEFGHIJKLMNOP')
    return ''.join((c for c in s if c not in chars_to_remove))