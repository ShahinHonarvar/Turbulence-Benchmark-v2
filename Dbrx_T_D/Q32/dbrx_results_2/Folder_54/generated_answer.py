def insert_after_character(s: str) -> str:
    return ''.join([char + 'f' if char == 'M' else char for char in s])