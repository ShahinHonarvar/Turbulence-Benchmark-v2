def insert_after_character(s: str) -> str:
    return s.replace('R', "R'V") if 'R' in s else s