def filter_chars(s: str) -> str:
    chars_to_remove = set((ord(c) for c in s[82:93] if ord('!') < ord(c) < ord('*')))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))