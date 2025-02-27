def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('!'), ord('@') + 1) if 11 <= i <= 32]
    return ''.join((c for c in s if c not in chars_to_remove))