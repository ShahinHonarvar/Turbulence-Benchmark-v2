def insert_before_character(s: str) -> str:
    return s.replace('r', 'wr', 1) if s[0] == 'r' else 'w' + s.replace('r', 'wr', 1)