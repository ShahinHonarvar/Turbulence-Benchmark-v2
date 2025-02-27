def filter_chars(s: str) -> str:
    chars_to_remove = {c for c in s if 10 <= s.index(c) <= 52 and ord('@') <= ord(c) <= ord('T')}
    return ''.join((c for c in s if c not in chars_to_remove))