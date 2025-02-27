def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[20:63] if 'i' <= char <= 'k']
    return s.replace(''.join(chars_to_remove), '')