def insert_before_character(s: str) -> str:
    return ''.join([char if char != 'I' else 'iI' for char in s])