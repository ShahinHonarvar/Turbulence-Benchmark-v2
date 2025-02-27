def insert_after_character(s: str) -> str:
    return ''.join([char + 'o' if char == ' ' else char for char in s])