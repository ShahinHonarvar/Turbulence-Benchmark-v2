def insert_after_character(input_string: str) -> str:
    return input_string.replace('T', 'T' + ' ', 1) if input_string.count('T') > 0 else input_string