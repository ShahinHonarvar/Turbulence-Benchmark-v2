def insert_before_character(s: str) -> str:
    return ''.join([char if char != 'P' else 'VP' for char in s])