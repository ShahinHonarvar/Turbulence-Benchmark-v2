def insert_before_character(s: str) -> str:
    return ''.join((char if char != 'g' else 'Mg' for char in s))