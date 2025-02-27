def insert_before_character(s: str) -> str:
    return s.replace('u', 'Uu').replace('UU', 'U')