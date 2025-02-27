def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[330:543])
    unique_chars = set(s) - repeat_chars
    return ''.join((c for c in s if c in unique_chars))