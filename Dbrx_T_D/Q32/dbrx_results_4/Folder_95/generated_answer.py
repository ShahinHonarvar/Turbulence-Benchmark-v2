def insert_after_character(s: str) -> str:
    return s.replace('j', 'j' + 'q', 1) if s.find('j') != -1 else s