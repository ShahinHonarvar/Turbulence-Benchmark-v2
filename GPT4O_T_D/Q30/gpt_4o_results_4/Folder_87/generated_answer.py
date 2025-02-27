def insert_before_character(s: str) -> str:
    return ''.join(('N' + char if char == 'm' else char for char in s))