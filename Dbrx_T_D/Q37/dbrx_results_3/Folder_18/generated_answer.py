def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('-'), ord('D') + 1))
    return ''.join((c for c in s if c >= '770' and c <= '970' and (ord(c) not in chars_to_remove)))