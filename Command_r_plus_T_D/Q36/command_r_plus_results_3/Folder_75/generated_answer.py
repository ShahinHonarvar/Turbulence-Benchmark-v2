def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(47, 75) if chr(i) > '&' and chr(i) < 'M']
    return ''.join((c for c in s if c not in chars_to_remove))