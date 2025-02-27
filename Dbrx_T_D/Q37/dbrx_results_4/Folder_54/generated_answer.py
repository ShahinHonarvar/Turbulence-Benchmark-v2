def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('-'), ord('X') + 1)).intersection(s[46:86])
    for c in chars_to_remove:
        s = s.replace(chr(c), '', 1)
    return s