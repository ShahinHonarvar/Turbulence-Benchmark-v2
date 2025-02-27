def insert_before_character(s: str) -> str:
    return s.replace('r', 'wr', 1) if s.startswith('r', 1) else s.replace('r', 'wr')