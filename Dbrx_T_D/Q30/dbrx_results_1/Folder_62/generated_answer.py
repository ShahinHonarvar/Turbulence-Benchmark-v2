def insert_before_character(s: str) -> str:
    return ''.join(['o' if c == ' ' else c for c in s]).replace(' ', 'o')