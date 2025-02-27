def insert_after_character(input_string: str) -> str:
    return input_string.replace('t', 'tG', 1) if input_string.count('t') > 0 else input_string