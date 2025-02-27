def insert_after_character(input_string: str) -> str:
    return input_string.replace('x', 'xN', 1) if input_string.count('x') else input_string