def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[35:90] if 'E' <= c <= 't']
    return s.translate(str.maketrans('', '', ''.join(chars_to_remove)))