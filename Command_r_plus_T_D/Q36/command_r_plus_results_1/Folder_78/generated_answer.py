def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(37, 65)]
    new_s = ''.join([c for c in s if c not in chars_to_remove or s.index(c) < 29 or s.index(c) > 33])
    return new_s