def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[384:412] if '/' <= c <= '8']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s