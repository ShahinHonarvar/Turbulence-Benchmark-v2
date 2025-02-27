def insert_after_character(s: str) -> str:
    return ''.join((char if char != 'X' else 'X6' for char in s))