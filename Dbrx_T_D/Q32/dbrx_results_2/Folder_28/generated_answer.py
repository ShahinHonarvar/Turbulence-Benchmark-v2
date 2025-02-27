def insert_after_character(s: str) -> str:
    return ''.join((char if char != 'r' else 'r1' for char in s))