def insert_before_character(s: str) -> str:
    return ''.join((char if char != 'O' else 'jO' for char in s))