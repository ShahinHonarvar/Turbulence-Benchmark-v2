def insert_after_character(s: str) -> str:
    return s.replace('r', 'rw', 1).replace('r', 'r', 1) if 'r' in s else s