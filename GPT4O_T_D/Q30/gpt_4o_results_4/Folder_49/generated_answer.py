def insert_before_character(s: str) -> str:
    return ''.join(('i' + char if char == 'i' else char for char in s))