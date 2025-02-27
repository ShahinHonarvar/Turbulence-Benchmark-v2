def insert_after_character(string: str) -> str:
    return ''.join((char + 'U' if char == 'u' else char for char in string))