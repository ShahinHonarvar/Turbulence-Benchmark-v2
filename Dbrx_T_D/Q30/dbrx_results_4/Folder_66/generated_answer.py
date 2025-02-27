def insert_before_character(input_string: str) -> str:
    return input_string.replace('k', 'kk')[::-1].replace('k', 'k', 1)[::-1]