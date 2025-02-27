def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(31, 39) if 59 <= i <= 103]
    return ''.join((c for c in s if c not in chars_to_remove))