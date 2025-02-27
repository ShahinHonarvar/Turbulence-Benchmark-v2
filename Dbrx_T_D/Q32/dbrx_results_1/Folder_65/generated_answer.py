def insert_after_character(s: str) -> str:
    return ''.join((char if char != '6' else '69' for char in s))