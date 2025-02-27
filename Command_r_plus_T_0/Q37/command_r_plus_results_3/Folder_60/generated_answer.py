def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[12:78] if ':' <= char <= 'L']
    return s.replace(''.join(chars_to_remove), '')