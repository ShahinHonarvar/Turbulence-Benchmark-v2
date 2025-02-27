def insert_after_character(input_string: str) -> str:
    return input_string.replace('x', 'xN', input_string.count('x') * len(input_string))