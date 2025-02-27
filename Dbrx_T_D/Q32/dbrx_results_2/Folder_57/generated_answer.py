def insert_after_character(s: str) -> str:
    return s.replace('s', 'sw', 1) if s.find('s') != -1 else s