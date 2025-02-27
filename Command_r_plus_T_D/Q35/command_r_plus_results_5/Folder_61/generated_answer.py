def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[0:9])
    return ''.join((c for c in s if c in unique_chars))