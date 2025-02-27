def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[42:67] if '6' < c < 'g']
    result = ''.join([c for c in s if c not in chars_to_remove])
    return result