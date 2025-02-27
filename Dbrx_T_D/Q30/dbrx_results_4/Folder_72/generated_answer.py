def insert_before_character(input_string: str) -> str:
    return ''.join((char if char != 'O' else 'dO' for char in input_string))