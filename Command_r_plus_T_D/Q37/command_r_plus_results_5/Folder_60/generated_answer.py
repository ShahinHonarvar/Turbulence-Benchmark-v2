def filter_chars(s: str) -> str:
    chars_to_remove = set(s[12:78]) & set(':-9;<=>?@ABCDEFGHIJKLM')
    return ''.join((c for c in s if c not in chars_to_remove))