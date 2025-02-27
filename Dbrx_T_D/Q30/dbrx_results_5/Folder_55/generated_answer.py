def insert_before_character(s: str) -> str:
    return s.replace('u', 'Uu', 1) if s and 'u' in s else s