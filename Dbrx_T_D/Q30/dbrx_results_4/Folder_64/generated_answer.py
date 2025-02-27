def insert_before_character(input_string: str) -> str:
    return input_string.replace('u', 'uu', input_string.count('u') * 2)