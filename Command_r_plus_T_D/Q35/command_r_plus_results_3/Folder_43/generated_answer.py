def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[10:28])
    unique_chars = set(s[10:28]) - set(s[10:28])
    return s[:10] + ''.join((c for c in s[10:28] if c in unique_chars)) + s[28:]