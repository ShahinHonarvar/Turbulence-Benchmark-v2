def insert_before_character(s: str) -> str:
    return ''.join(['t' if c == 'a' else c for c in s])