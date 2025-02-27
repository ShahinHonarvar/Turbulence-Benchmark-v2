def insert_after_character(input_string: str) -> str:
    return input_string.replace('k', 'k' + 'k', len(input_string) - 1)