def insert_before_character(s: str) -> str:
    return s.replace('c', 'Gc') if 'c' in s else s