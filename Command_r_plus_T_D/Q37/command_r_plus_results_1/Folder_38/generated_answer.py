def filter_chars(s: str) -> str:
    chars_to_remove = [ch for ch in s[24:80] if 'a' <= ch <= 'f']
    return s.translate(str.maketrans('', '', ''.join(chars_to_remove)))