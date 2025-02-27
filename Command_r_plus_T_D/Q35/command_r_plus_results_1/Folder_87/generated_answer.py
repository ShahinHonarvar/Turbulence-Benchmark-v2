def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[20:43])
    unique_chars = set(s[20:43]) - repeat_chars
    return s[:20] + ''.join((c for c in s[20:43] if c in unique_chars)) + s[43:]