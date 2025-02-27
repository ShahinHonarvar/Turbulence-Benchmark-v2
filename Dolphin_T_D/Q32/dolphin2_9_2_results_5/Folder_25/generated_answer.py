def insert_after_character(s: str) -> str:
    return ''.join(('W' if c == 'e' else c for c in s))