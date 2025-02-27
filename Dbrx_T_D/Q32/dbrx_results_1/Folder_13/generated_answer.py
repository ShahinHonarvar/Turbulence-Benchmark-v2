def insert_after_character(input_string: str) -> str:
    return ''.join([char + 'N' if char == 'x' else char for char in input_string])