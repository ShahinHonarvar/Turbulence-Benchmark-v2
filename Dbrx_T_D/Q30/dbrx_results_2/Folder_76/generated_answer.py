def insert_before_character(s: str) -> str:
    return ''.join(['m' + char if char == 'F' else char for char in s])