def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[587:648] if c > ',' and c < 'c']
    result = ''.join([c for c in s if c not in chars_to_remove])
    return result