def insert_before_character(input_string: str) -> str:
    return ''.join([char if char != 'a' else 'Wa' for char in input_string])