def insert_before_character(input_string: str) -> str:
    return ''.join(['E' if char == 'e' else char for char in input_string])