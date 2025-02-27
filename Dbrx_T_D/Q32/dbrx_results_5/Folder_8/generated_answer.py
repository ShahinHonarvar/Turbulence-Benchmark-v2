def insert_after_character(input_string: str) -> str:
    return input_string.replace('E', 'E' + 'T', input_string.count('E'))