def insert_before_character(s: str) -> str:
    return ''.join((char if char != 'r' else '1' + char for char in s))