def insert_after_character(input_string: str) -> str:
    return input_string.replace('O', 'O' + 'O', 1) if 'O' in input_string else input_string