def insert_after_character(s: str) -> str:
    return ''.join((char if char != ' ' else 'P ' for char in s))