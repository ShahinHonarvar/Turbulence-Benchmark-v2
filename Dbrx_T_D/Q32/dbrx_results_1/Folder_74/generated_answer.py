def insert_after_character(input_string: str) -> str:
    return input_string.replace('T', 'T ') if 'T' in input_string else input_string