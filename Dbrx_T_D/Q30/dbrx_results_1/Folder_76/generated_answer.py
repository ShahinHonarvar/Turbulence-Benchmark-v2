def insert_before_character(s: str) -> str:
    return ''.join(['m' if c == 'F' else c for c in s])