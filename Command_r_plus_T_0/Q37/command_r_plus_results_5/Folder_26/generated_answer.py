def filter_chars(s: str) -> str:
    chars_to_remove = [ch for ch in s[20:63] if 'i' <= ch <= 'k']
    return s.replace(''.join(chars_to_remove), '')