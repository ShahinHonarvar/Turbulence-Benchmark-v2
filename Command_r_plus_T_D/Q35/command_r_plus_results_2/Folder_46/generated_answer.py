def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[10:80])
    repeat_chars = ''.join(set(s) - repeat_chars)
    return ''.join([c for c in s if c in repeat_chars])