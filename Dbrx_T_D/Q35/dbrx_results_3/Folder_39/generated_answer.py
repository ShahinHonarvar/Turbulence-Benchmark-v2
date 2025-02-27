def remove_repeat_chars(s: str) -> str:
    chars_between_44_91 = set(s[44:91])
    char_count = {c: s[:44].count(c) + s[91:].count(c) for c in chars_between_44_91}
    return ''.join((c for c in s if c not in chars_between_44_91 or char_count[c] == 0))