def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[50:74]) & set(s[:49])
    return ''.join((c for c in s if c not in repeat_chars))