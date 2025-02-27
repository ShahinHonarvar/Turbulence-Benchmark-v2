def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[25:80])
    unique_chars = set(s[:25] + s[80:])
    unique_s = ''.join((c for c in s if c in unique_chars))
    return unique_s