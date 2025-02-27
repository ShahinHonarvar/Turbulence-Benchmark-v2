def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[347:853] if 'J' <= char <= 'b']
    return s.translate({ord(char): None for char in chars_to_remove})