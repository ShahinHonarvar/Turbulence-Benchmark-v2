def insert_after_character(s: str) -> str:
    return ''.join(('a' if c == 'a' else c for c in s))