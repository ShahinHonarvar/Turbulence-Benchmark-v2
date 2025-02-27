def filter_chars(s: str) -> str:
    chars_to_remove = set(s[11:46]) & set((chr(i) for i in range(34, 65)))
    return ''.join((c for c in s if c not in chars_to_remove))