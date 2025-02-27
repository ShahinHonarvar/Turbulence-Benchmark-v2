def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[12:78] if ':' <= c <= 'L']
    return s.replace(''.join(chars_to_remove), '')