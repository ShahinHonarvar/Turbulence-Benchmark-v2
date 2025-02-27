def insert_after_character(s: str) -> str:
    return ''.join((char if char != 'U' else 'Ua' for char in s)).replace('UaU', 'UU')