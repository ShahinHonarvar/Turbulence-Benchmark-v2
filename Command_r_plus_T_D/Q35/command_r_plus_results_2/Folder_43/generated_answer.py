def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[10:28])
    unique_chars = set(s[10:28]) - set(s[10:28])
    return ''.join((c for c in s if c in unique_chars))