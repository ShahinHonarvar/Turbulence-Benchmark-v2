def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[200:203])
    return ''.join((c for i, c in enumerate(s) if i < 200 or c in unique_chars))